from libqtile.backend.base import Window
from libqtile.config import Screen
from libqtile.core.manager import Qtile
from libqtile.group import _Group  # noqa


def move_window_to_screen(qtile: Qtile, window: Window, screen: Screen):
    """Moves a window to a screen and focuses it, allowing you to move it
    further if you wish."""
    window.togroup(screen.group.name)
    qtile.focus_screen(screen.index)
    screen.group.focus(window, True)


# If a group is currently being toggled or not.
toggling_groups: dict[str, bool] = {}
# A group => windows mapping to remember where a window came from when toggling its group
group_windows: dict[str, list[Window]] = {}


def toggle_group(qtile: Qtile, clicked_group: _Group):
    """
    Bring the given group's windows to the current group, essentially combining them
    """
    current_group = qtile.current_group

    was_toggling = toggling_groups.get(clicked_group.name, False)
    toggling_groups[clicked_group.name] = not was_toggling

    if was_toggling:
        # Send proper windows back to clicked_group
        original_windows = group_windows[clicked_group.name]
        # We need to filter out any deleted windows
        windows_to_send_back = [win for win in current_group.windows if win in original_windows]
        # `reversed` works with `clicked_group.windows[-1]` bellow to keep ordering at least
        # when returning windows to their og group
        for win in reversed(windows_to_send_back):
            win.togroup(clicked_group.name)

        group_windows[clicked_group.name] = []
    else:
        # Bring windows from clicked_group to current group
        group_windows[clicked_group.name] = []

        # `last_length` is used to make sure there is a window moving each time,
        # otherwise we are in an infinite loop
        last_length = len(clicked_group.windows)
        while len(clicked_group.windows) > 0:
            win: Window = clicked_group.windows[-1]

            group_windows[clicked_group.name].append(win)
            win.togroup(current_group.name)

            if last_length == len(clicked_group.windows):
                qtile.cmd_spawn(f'notify-send "Qtile Warning: could not toggle group `{clicked_group.name}`"')
                break
            last_length = len(clicked_group.windows)
