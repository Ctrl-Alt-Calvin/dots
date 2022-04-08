#!/usr/bin/env bash
#
picom --config ~/.config/picom/picom.conf --vsync &
#
#Dual Monitor Xrandr Setup
#xrandr --output DisplayPort-0 --primary --mode 1920x1080 --rate 144 --output DisplayPort-2 --mode 1920x1080 --rate 144 --left-of DisplayPort-0
#
#Single Monitor
xrandr --output DisplayPort-2 --mode 1920x1080 --rate 239.76 --primary
feh --bg-fill ~/.config/wallpapers/mountainscape-wallpaper.jpg
