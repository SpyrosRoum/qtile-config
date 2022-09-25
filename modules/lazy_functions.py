from libqtile.lazy import lazy

from modules.utils import move_window_to_screen


@lazy.function
def move_window_to_prev_screen(qtile):
    """Moves a window to the previous screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index - 1 if index > 0 else len(qtile.screens) - 1
    move_window_to_screen(qtile, qtile.current_window, qtile.screens[index])


@lazy.function
def move_window_to_next_screen(qtile):
    """Moves a window to the next screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index + 1 if index < len(qtile.screens) - 1 else 0
    move_window_to_screen(qtile, qtile.current_window, qtile.screens[index])


@lazy.function
def move_focus_to_prev_screen(qtile):
    """Moves the focus to the previous screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index - 1 if index > 0 else len(qtile.screens) - 1
    qtile.focus_screen(qtile.screens[index].index)


@lazy.function
def move_focus_to_next_screen(qtile):
    """Moves the focus to the next screen. Loops around the beginning and
    end."""
    index = qtile.current_screen.index
    index = index + 1 if index < len(qtile.screens) - 1 else 0
    qtile.focus_screen(qtile.screens[index].index)
