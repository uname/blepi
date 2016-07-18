#-*- coding: utf-8 -*-
from bluepy.btle import Scanner, DefaultDelegate
from SigObject import sigObject
from log import logger
import signals

class ScanDelegate(DefaultDelegate):
    
    def __init__(self):
        DefaultDelegate.__init__(self)
        
    def handleDiscovery(self, dev, isNewDev, isNewData):
        #logger.debug("%s[%d]" % (dev.addr, dev.rssi))
        sigObject.emit(signals.BLE_INFO_UPDATE, dev.addr, dev.rssi)

if __name__ == "__main__":
    from bluepy.btle import Scanner
    scanner = Scanner().withDelegate(ScanDelegate())
    scanner.scan(4)
