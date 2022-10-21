from libqtile import qtile
from libqtile.core.manager import Qtile
from libqtile.group import _Group  # noqa
from libqtile.lazy import lazy
from libqtile.widget import GroupBox

from modules.utils import move_window_to_screen
from modules.state import toggling_state

qtile: Qtile = qtile


@lazy.function
def move_window_to_prev_screen(_):
    """Moves a window to the previous screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index - 1 if index > 0 else len(qtile.screens) - 1
    move_window_to_screen(qtile, qtile.current_window, qtile.screens[index])


@lazy.function
def move_window_to_next_screen(_):
    """Moves a window to the next screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index + 1 if index < len(qtile.screens) - 1 else 0
    move_window_to_screen(qtile, qtile.current_window, qtile.screens[index])


@lazy.function
def move_focus_to_prev_screen(_):
    """Moves the focus to the previous screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index - 1 if index > 0 else len(qtile.screens) - 1
    qtile.focus_screen(qtile.screens[index].index)


@lazy.function
def move_focus_to_next_screen(_):
    """Moves the focus to the next screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index + 1 if index < len(qtile.screens) - 1 else 0
    qtile.focus_screen(qtile.screens[index].index)


def groupbox_toggle_group(group_box: GroupBox):
    clicked_group: _Group = group_box.get_clicked_group()
    toggling_state.toggle_group(clicked_group)


def groupbox_reset_toggling_group(group_box: GroupBox):
    clicked_group: _Group = group_box.get_clicked_group()
    if clicked_group == qtile.current_group:
        toggling_state.reset_toggled(clicked_group)
    else:
        group_box.bar.screen.set_group(clicked_group, warp=False)
