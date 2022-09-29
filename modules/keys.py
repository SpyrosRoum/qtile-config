from libqtile.config import Key
from libqtile.lazy import lazy

from modules.common import mod, terminal
from modules.lazy_functions import (move_focus_to_next_screen,
                                    move_focus_to_prev_screen,
                                    move_window_to_next_screen,
                                    move_window_to_prev_screen)

keys = [
    # Switch focus between windows/screens
    Key([mod], "h", move_focus_to_prev_screen, desc="Move focus to left"),
    Key([mod], "l", move_focus_to_next_screen, desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows
    Key(
        [mod, "shift"],
        "h",
        move_window_to_prev_screen,
        desc="Move window to the previous screen",
    ),
    Key(
        [mod, "shift"],
        "l",
        move_window_to_next_screen,
        desc="Move window to the next screen",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.swap_main(),
        desc="Swap current window to main pane",
    ),

    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # # Grow windows. If current window is on the edge of screen and direction
    # # will be to screen edge - window would shrink.
    # Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    # Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    # Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [mod, "shift"],
        "space",
        lazy.window.toggle_floating(),
        desc="Toggle the floating state of the window."
    ),

    # Qtile
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

spawn_apps = [
    # ===== Core =====
    Key(
        [mod],
        "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
    ),
    Key(
        [mod],
        "s",
        lazy.spawn("rofi -show-icons -icon-theme \"Papirus\" -show drun -font \"Fira Code 12\""),
        desc="Spawn rofi"
    ),

    # ===== Browser =====
    Key(
        [mod],
        "w",
        lazy.spawn("firefox -P default"),
        desc="Launch Firefox"
    ),
    Key(
        [mod, "shift"],
        "w",
        lazy.spawn("firefox -P default --private-window"),
        desc="Launch Firefox"
    ),

    # ===== Misc Apps =====
    Key(
        [mod],
        "d",
        lazy.spawn("discord-canary"),
        desc="Launch discord"
    ),
    Key(
        [mod],
        "m",
        lazy.spawn("spotify"),
        desc="Launch Spotify"
    ),
    Key(
        [mod],
        "g",
        lazy.spawn("steam"),
        desc="Launch Steam"
    ),
    Key(
        [mod],
        "p",
        lazy.spawn("pavucontrol"),
        desc="Launch Pavucontrol"
    ),

    # ===== Scripts =====
    Key(
        [mod],
        "v",
        lazy.spawn("clipmenu"),
        desc="Spawn clipmenu"
    ),
    Key(
        [mod],
        "semicolon",
        lazy.spawn("sh /home/spyros/.local/bin/dmenuunicode"),
        desc="Spawn emoji picker"
    ),
    # Button10 is handled from sxhkd
    # Key(
    #     [],
    #     "Button10",
    #     lazy.spawn("bash /home/spyros/.local/bin/output_switcher"),
    #     desc="Switch sound output"
    # ),
    Key(
        ["mod1"],
        "l",
        lazy.spawn("light-locker-command -l"),
        desc="Lock Screen"
    ),

    # ===== Media Control =====
    # Volume
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pulsemixer --change-volume +5 --unmute"),
        desc="Raise volume"
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pulsemixer --change-volume -5 --unmute"),
        desc="Lower volume"
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pulsemixer --toggle-mute"),
        desc="Toggle mute"
    ),
    # Prev/Next
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn("playerctl --all-players next"),
        desc="Next track"
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl --all-players previous"),
        desc="Prev Track"
    ),
    # Pause/Play
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl --all-players play-pause"),
        desc="Play/Pause"
    ),

    # ===== Screenshot =====
    Key(
        [],
        "Print",
        lazy.spawn("flameshot gui"),
        desc="Print-screen area"
    ),
    Key(
        ["control"],
        "Print",
        lazy.spawn("flameshot full -c -p /home/spyros/Pictures/Screenshots"),
        desc="Print-screen full-screen"
    ),
]

keys.extend(spawn_apps)
