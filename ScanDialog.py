#-*- coding: utf-8 -*-
from view.Ui_ScanDialog import Ui_ScanDialog
from PyQt4 import QtGui

class ScanDialog(QtGui.QDialog):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        
        self.setupUi()
        
    def setupUi(self):
        self.setModal(True)
        self.ui = Ui_ScanDialog()
        self.ui.setupUi(self)
        