#!/usr/bin/env bash
wget -O /tmp/update_information_writer.py "https://raw.githubusercontent.com/antony-jr/appimage-update-info-writer/main/update_info_writer.py"
chmod +x /tmp/update_information_writer.py

/tmp/update_information_writer.py FreeCAD_0.19-*glibc2.12-x86_64.AppImage "gh-releases-zsync|FreeCAD|FreeCAD|0.19_pre|FreeCAD*glibc2.12-x86_64.AppImage.zsync"

rm -rf /tmp/update_information_writer.py

