from libqtile import hook
from libqtile import qtile
from libqtile.core.manager import Qtile

from modules.state import toggling_state

qtile: Qtile = qtile


@hook.subscribe.setgroup
def reset_toggling_on_group_change():
    """
    Essentially when we change group we want to reset all toggling
    """
    prev_group = qtile.current_screen.previous_group
    toggling_state.reset_toggled(prev_group)
