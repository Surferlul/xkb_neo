# xkb_neo
My xkb modifications for making neo etc (inclusive vou) work properly with every part of GNU/Linux. YES, even Java Applications.

For programs running through XWayland manually execute

~~~bash
setxkbmap de vou
~~~

to get proper keybindings working.

Execute patch.py to patch your system.

Or Manually:
- execute patch_xkb.py as superuser to patch /usr/share/X11/xkb.
- execute enable_gnome.sh as normal user to enable alternative keyboard layouts on GNOME
