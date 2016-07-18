#-*- coding: utf-8 -*-
from bluepy.btle import Scanner, DefaultDelegate
from log import logger

class ScanDelegate(DefaultDelegate):
    
    def __init__(self):
        DefaultDelegate.__init__(self)
        
    def handleDiscovery(self, dev, isNewDev, isNewData):
        logger.debug("%d[%d]" % (dev.addr, dev.rssi))
        