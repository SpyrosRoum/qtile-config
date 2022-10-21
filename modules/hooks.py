from libqtile import hook
from libqtile import qtile
from libqtile.core.manager import Qtile

from modules.state import toggling_state

qtile: Qtile = qtile


@hook.subscribe.current_screen_change
def ignore_setgroup_on_screen_change():
    """
    This event gets triggered before setgroup, so we can use this to ignore setgroup
    """
    toggling_state.changed_screen = True


@hook.subscribe.setgroup
def reset_toggling_on_group_change():
    """
    Essentially when we change group we want to reset all toggling
    """
    if toggling_state.changed_screen:
        toggling_state.changed_screen = False
        return

    prev_group = qtile.current_screen.previous_group

    if prev_group is None:
        # On start-up this is None
        return

    toggling_state.reset_toggled(prev_group)
