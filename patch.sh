#!/usr/bin/env bash

if [ "$EUID" -eq 0 ]
  then echo "Please don't run as root"
  exit
fi

BASEDIR=$(dirname "$0")
sudo python3 $BASEDIR/patch_xkb.py
bash $BASEDIR/enable_gnome.sh
