#!/usr/bin/env python2
from xdg.IconTheme import *

print getIconPath("opera")

theme = IconTheme()
theme.parse("/usr/kde/3.1/share/icons/hicolor/index.desktop")
theme.validate()