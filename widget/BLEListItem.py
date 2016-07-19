#-*- coding: utf-8 -*-
from icons.icons import *
from PyQt4 import QtGui

class BLEListItem(QtGui.QListWidgetItem):
    
    def __init__(self, addr, rssi):
        QtGui.QListWidgetItem.__init__(self)
        self.addr, self.rssi = addr, rssi
        self.__update()
        
    def __update(self):
        iconPath = ":app/icons/app/sig_1.png"
        if   self.rssi > -45:
            iconPath = ":app/icons/app/sig_4.png"
        elif self.rssi > -60:
            iconPath = ":app/icons/app/sig_3.png"
        elif self.rssi > -80:
            iconPath = ":app/icons/app/sig_2.png"
            
        self.setIcon(QtGui.QIcon(iconPath))
        self.setText("%s\t\t\t\t%ddb" % (self.addr, self.rssi))
    
    def updateRssi(self, rssi):
        self.rssi = rssi
        self.__update()