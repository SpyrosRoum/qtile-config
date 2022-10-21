from libqtile.backend.base import Window
from libqtile.core.manager import Qtile
from libqtile import qtile as q
from libqtile.group import _Group  # noqa

from modules.utils import notify


class TogglingState:
    def __init__(self, qtile: Qtile):
        # If a group is currently being toggled or not.
        self.toggling_groups: dict[str, bool] = {}
        # A group => windows mapping to remember where a window came from when toggling its group
        self.group_windows: dict[str, list[Window]] = {}

        self.qtile = qtile

    def toggle_group(self, group: _Group):
        """
        Bring the given group's windows to the current group, essentially combining them
        """
        current_group = self.qtile.current_group

        was_toggling = self.toggling_groups.get(group.name, False)
        self.toggling_groups[group.name] = not was_toggling

        if was_toggling:
            # Send proper windows back to clicked_group
            original_windows = self.group_windows[group.name]
            # We need to filter out any deleted windows
            windows_to_send_back = [
                win for win in current_group.windows if win in original_windows
            ]
            # `reversed` works with `clicked_group.windows[-1]` bellow to keep ordering at least
            # when returning windows to their og group
            for win in reversed(windows_to_send_back):
                win.togroup(group.name)

            self.group_windows[group.name] = []
        else:
            # Bring windows from clicked_group to current group
            self.group_windows[group.name] = []

            # `last_length` is used to make sure there is a window moving each time,
            # otherwise we are in an infinite loop
            last_length = len(group.windows)
            while len(group.windows) > 0:
                win: Window = group.windows[-1]

                self.group_windows[group.name].append(win)
                win.togroup(current_group.name)

                if last_length == len(group.windows):
                    notify(f"Qtile Warning: could not toggle group `{group.name}`")
                    break
                last_length = len(group.windows)

    def reset_toggled(self, focused_group: _Group):
        """
        Reset all toggling groups
        """
        for group, toggling in self.toggling_groups.items():
            if toggling:
                og_windows = self.group_windows[group]
                windows_to_send_back = [win for win in focused_group.windows if win in og_windows]
                for win in reversed(windows_to_send_back):
                    win.togroup(group, switch_group=False)

                self.group_windows[group] = []
                self.toggling_groups[group] = False


toggling_state = TogglingState(q)
