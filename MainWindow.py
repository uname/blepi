#-*- coding: utf-8 -*-
from view.Ui_MainWindow import Ui_MainWindow
from ScanDialog import ScanDialog
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.setupUi()
        self.setupSignals()
    
    def setupUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scanDialog = ScanDialog(self)
        
    def setupSignals(self):
        self.ui.scanButton.clicked.connect(self.onScanButtonClicked)
        
    
    def onScanButtonClicked(self):
        self.scanDialog.show_()