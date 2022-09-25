import os
import platform

host = platform.node()

IS_XEPHYR: bool = int(os.environ.get("QTILE_XEPHYR", 0)) > 0
if IS_XEPHYR:
    mod = "mod1"
else:
    mod = "mod4"

terminal = "alacritty"
