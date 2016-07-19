@echo off
python genqrc.py ../icons ../../icons/icons.py
del /Q AppIcons.qrc
