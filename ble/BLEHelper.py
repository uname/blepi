#-*- coding: utf-8 -*-
from bluepy.btle import Scanner
from ScanDelegate import ScanDelegate

class BLEHelper(object):
    
    def __init__(self):
        self.scanner = Scanner().withDelegate(ScanDelegate())
        
    def startScan(self, timeout=10):
        self.scanner.scan(timeout)
        
    def stopScan(self):
        self.scanner.stop()
        
        
    
    
bleHelper = BLEHelper()
