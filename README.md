# xkb_neo
My xkb modifications for making neo etc (inclusive vou) work properly with every part of GNU/Linux. On X11 this works for all programs, on Wayland on the other hand, some Programs (for example Java applications) will not properly read some inputs.

Execute patch.py to patch your system.

Or Manually:
- execute patch_xkb.py as superuser to patch /usr/share/X11/xkb.
- execute enable_gnome.sh as normal user to enable alternative keyboard layouts on GNOME
