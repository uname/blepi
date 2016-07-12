#-*- coding: utf-8 -*-
from PyQt4 import QtGui

class BLEListWidget(QtGui.QListWidget):
    
    def __init__(self, parent=None):
        QtGui.QListWidget.__init__(self)