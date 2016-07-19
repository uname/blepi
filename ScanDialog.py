#-*- coding: utf-8 -*-
from view.Ui_ScanDialog import Ui_ScanDialog
from delegate.ScanDialogDelegate import ScanDialogDelegate
from SigObject import sigObject
from log import logger
from PyQt4 import QtGui

import signals


class ScanDialog(QtGui.QDialog):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        
        self.setupUi()
        self.setupSignals()
        
        self.delegate = ScanDialogDelegate()
        
    def setupUi(self):
        self.setModal(True)
        self.ui = Ui_ScanDialog()
        self.ui.setupUi(self)
    
    def setupSignals(self):
        self.ui.cancelButton.clicked.connect(self.onCancelButtonClicked)
        self.connect(sigObject, signals.BLE_INFO_UPDATE, self.onBLEInfoUpdate)
    
    def onBLEInfoUpdate(self, addr, rssi):
        logger.debug("BLE -> %s(%d)" % (addr, rssi))
        self.ui.bleListWidget.updateBLEDevice(addr, rssi)
        
    def setUiOnShow(self):
        self.ui.tipLabel.setText("Scanning...")
        
    def onCancelButtonClicked(self):
        self.close()
        
    def show_(self):
        self.setUiOnShow()
        self.show()
        
        self.delegate.startBLEScan()