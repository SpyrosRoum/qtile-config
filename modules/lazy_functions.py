from libqtile import qtile
from libqtile.core.manager import Qtile
from libqtile.group import _Group  # noqa
from libqtile.lazy import lazy
from libqtile.widget import GroupBox

from modules.utils import move_window_to_screen, toggle_group, reset_toggled

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


@lazy.widget["box1"].function
def groupbox_toggle_group_box1(group_box: GroupBox):
    clicked_group: _Group = group_box.get_clicked_group()
    toggle_group(qtile, clicked_group)


@lazy.widget["box2"].function
def groupbox_toggle_group_box2(group_box: GroupBox):
    clicked_group: _Group = group_box.get_clicked_group()
    toggle_group(qtile, clicked_group)


@lazy.widget["box1"].function
def groupbox_reset_toggling_group_box1(group_box: GroupBox):
    clicked_group: _Group = group_box.get_clicked_group()
    if clicked_group == qtile.current_group:
        reset_toggled(clicked_group)
    else:
        group_box.bar.screen.set_group(clicked_group, warp=False)


@lazy.widget["box2"].function
def groupbox_reset_toggling_group_box2(group_box: GroupBox):
    clicked_group: _Group = group_box.get_clicked_group()
    if clicked_group == qtile.current_group:
        reset_toggled(clicked_group)
    else:
        group_box.bar.screen.set_group(clicked_group, warp=False)
