# YN360 Bluetooth Control for Mac
Example python scripts to control your Yongnuo RGB Lights from your Mac via Bluetooth Low-Energy on macOS.

Similar to [Lantern library by Ken Keitner](https://github.com/kenkeiter/lantern/blob/master/lantern/color.py), except this supports MacOS.

If you are looking for a nice interface to control these lights, you may also like to check out my [YN360_BTLE project](https://github.com/pinchies/YN360_webbtle), which supports WebBT across multiple platforms, including the Chrome web browser on Mac.

## Supported Yongnuo devices with Bluetooth control
### RGB / White Light Wands
- [Yongnuo YN360](https://amzn.to/3ECcUiD)
- [Yongnuo YN360 II](https://amzn.to/3MmzHRg)
- [Yongnuo YN360 III](https://amzn.to/3Tb4Pp5)
- [Yongnuo YN360 III Pro](https://amzn.to/3rNsFM6)
- [Yongnuo YN660](https://amzn.to/3rRs0Jm)
- [Yongnuo YN860 Pro](https://amzn.to/3CY5mFX)
- [Yongnuo YN30SOFT](https://amzn.to/3Mlf08t)
- [Yongnuo YN60 Pro](https://amzn.to/3fY5z2O)
- [Yongnuo YN360Mini](https://amzn.to/3CQQXLG)

### White LED Video Light Panels
- [Yongnuo YN300 III](https://amzn.to/3ywJsGU)
- [Yongnuo YN300 IV](https://amzn.to/3CY3IUN)
- [Yongnuo YN600L II](https://amzn.to/3yvt6yc)
- [Yongnuo YN900](https://amzn.to/3RQLJ6H)
- [Yongnuo YN900 Pro](https://amzn.to/3g0UbDi)
- [Yongnuo YN1200 Pro](https://amzn.to/3rPt4h7)
- [Yongnuo YN6000](https://amzn.to/3g11tqF)
- [Yongnuo YN9000](https://amzn.to/3rOxXqw)

### Studio White Lights with Bluetooth
- [Yongnuo YN760 Pro LED Light](https://amzn.to/3EDwOKl)
- [Yongnuo YNFLEX180 Flexible LED Photo Studio Light](https://amzn.to/3SR6e4s)
- [Yongnuo YNRAY180 LED Video Light](https://amzn.to/3CnquUw)
- [Yongnuo LUX160 LED Bowen Video Light](https://amzn.to/3EydvSj)

### RGB / White Ring Light 
- [YONGNUO YN508S](https://amzn.to/3EPiq1J)
- [YONGNUO YN508 Pro](https://amzn.to/3fNQ11i)

## Requirements: 
1. Python 3
2. [Bleak bluetooth library](https://pypi.org/project/bleak/)

## Usage:
1. Run the script to discover your device's bluetooth UUID.
2. Replace the UUID in the other scripts with your device's UUID
3. Run the script, with command line parameters to set the values of your light, e.g.:

To set the power of the warm and cool tone LEDs to 25% and 40% respectively:
$ python3 lights_settone.py 25 40 

To set the colour RGB LEDs to 14% red, 30% green, and 60% blue:
$ python3 lights_setrgb.py 14 30 60
