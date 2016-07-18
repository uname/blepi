#-*- coding: utf-8 -*-
from bluepy.btle import Scanner
from ScanDelegate import ScanDelegate
import threading

class BLEHelper(object):
    
    def __init__(self):
        self.scanThread = None
        self.scanner = Scanner().withDelegate(ScanDelegate())
    
    def __scanInThread(self, timeout):
        self.scanThread = threading.Thread(target=self.scanner.scan, args=(timeout,))
        self.scanThread.start()
        return True
        
    def startScan(self, timeout=10):
        if self.scanThread is None:
            return self.__scanInThread(timeout)
        else:
            if self.scanThread.is_alive():
                return False
            else:
                self.scanThread = None
                return self.startScan(timeout)
        
    def stopScan(self):
        self.scanner.stop()
        
        
    
    
bleHelper = BLEHelper()
