from libqtile import hook
from libqtile import qtile
from libqtile.core.manager import Qtile

from modules.utils import reset_toggled

qtile: Qtile = qtile


@hook.subscribe.setgroup
def reset_toggling_on_group_change():
    """
    Essentially when we change group we want to reset all toggling
    """
    prev_group = qtile.current_screen.previous_group
    reset_toggled(prev_group)
