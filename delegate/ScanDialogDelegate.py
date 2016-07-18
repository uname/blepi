#-*- coding: utf-8 -*-
from ble.BLEHelper import bleHelper

class ScanDialogDelegate(object):

    def __init__(self):
        pass
        
    def startBLEScan(self):
        bleHelper.startScan()