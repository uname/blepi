#-*- coding: utf-8 -*-
from PyQt4 import QtGui
from widget.BLEListItem import BLEListItem
from log import logger

class BLEListWidget(QtGui.QListWidget):
    
    def __init__(self, parent=None):
        QtGui.QListWidget.__init__(self)
        self.bleDict = {}
		
    def updateBLEDevice(self, addr, rssi):
        if not isinstance(addr, basestring):
            logger.warning("addr in updateBLEDevice should be basestring")
            return
        
        item = self.bleDict.get(addr)
        if item is None:
            item = BLEListItem(addr, rssi)
            self.bleDict[addr] = item
            self.addItem(item)
        else:
            item.updateRssi(rssi)
        
