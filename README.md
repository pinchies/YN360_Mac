# YN360 Mac
Example python scripts to control your Yongnuo RGB Lights (e.g. YN360 wand, YN600L II panel) via Bluetooth Low-Energy in Mac OS X.

Similar to [Lantern library by Ken Keitner](https://github.com/kenkeiter/lantern/blob/master/lantern/color.py), and similar to my own [YN360_BTLE](https://github.com/pinchies/YN360_webbtle), these scripts enable you to control the lights from your Mac.

Requirements: 
1. Python 3
2. [Bleak bluetooth library](https://pypi.org/project/bleak/)

Usage:
1. Run the script to discover your device's bluetooth UUID.
2. Replace the UUID in the other scripts with your device's UUID
3. Run the script, with command line parameters to set the values of your light, e.g.:

To set the power of the warm and cool tone LEDs to 25% and 40% respectively:
$ python3 lights_settone.py 25 40 

To set the colour RGB LEDs to 14% red, 30% green, and 60% blue:
$ python3 lights_setrgb.py 14 30 60
