"""
My Qtile config!
"""
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Match, Screen
from libqtile.lazy import lazy

from modules.common import mod
from modules.groups import group_keys, groups  # noqa
from modules.keys import keys
from modules.lazy_functions import (groupbox_toggle_group_box1,
                                    groupbox_toggle_group_box2)

keys.extend(group_keys)

# ===== Layouts =====
layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": "e1acff",
    "border_normal": "1D2330"
}

layouts = [
    layout.MonadTall(single_border_width=0, new_client_position="top", single_margin=0, **layout_theme),
    layout.Floating(**layout_theme),
    layout.Max(margin=0, border_width=0),
]

# ===== Widgets =====
widget_defaults = dict(
    font="ubuntu-mono-nerd",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    name="box1",
                    margin_x=1,
                    mouse_callbacks={"Button3": groupbox_toggle_group_box1},
                    disable_drag=True,
                    highlight_method='line'
                ),
                widget.CurrentLayoutIcon(padding=10),
                widget.WindowName(),
                widget.Mpris2(
                    scroll=False,
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=["xesam:artist", "xesam:title"]
                ),
                widget.Memory(fmt="🧠 {}", measure_mem="G"),
                widget.Sep(padding=10),
                widget.PulseVolume(step=5, fmt="🔊 {}", limit_max_volume=True),
                widget.Sep(padding=10),
                widget.Clock(fmt="📆 {}", format="%a, %b %d %Y, %H:%M%p"),
                widget.Sep(padding=10),
                widget.Systray(),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    name="box2",
                    margin_x=1,
                    mouse_callbacks={"Button3": groupbox_toggle_group_box2},
                    disable_drag=True,
                    highlight_method='line'
                ),
                widget.CurrentLayoutIcon(padding=10),
                widget.WindowName(),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                widget.Mpris2(
                    scroll=False,
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=["xesam:artist", "xesam:title"]
                ),
                widget.Memory(fmt="🧠 {}", measure_mem="G"),
                widget.Sep(padding=10),
                widget.PulseVolume(step=5, fmt="🔊 {}", limit_max_volume=True),
                widget.Sep(padding=10),
                widget.Clock(fmt="📆 {}", format="%a, %b %d %Y, %H:%M%p"),
                widget.Sep(padding=10),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size(), warp_pointer=True
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
