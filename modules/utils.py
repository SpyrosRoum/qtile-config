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


def notify(txt: str):
    from libqtile import qtile

    qtile.cmd_spawn(f'notify-send "{txt}"')
