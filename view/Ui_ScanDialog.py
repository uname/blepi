# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/scan_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ScanDialog(object):
    def setupUi(self, ScanDialog):
        ScanDialog.setObjectName(_fromUtf8("ScanDialog"))
        ScanDialog.resize(532, 304)
        self.gridLayout = QtGui.QGridLayout(ScanDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tipLabel = QtGui.QLabel(ScanDialog)
        self.tipLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tipLabel.setObjectName(_fromUtf8("tipLabel"))
        self.gridLayout.addWidget(self.tipLabel, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(430, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.cancelButton = QtGui.QPushButton(ScanDialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 2, 1, 1, 1)
        self.bleListWidget = BLEListWidget(ScanDialog)
        self.bleListWidget.setObjectName(_fromUtf8("bleListWidget"))
        self.gridLayout.addWidget(self.bleListWidget, 1, 0, 1, 2)

        self.retranslateUi(ScanDialog)
        QtCore.QMetaObject.connectSlotsByName(ScanDialog)

    def retranslateUi(self, ScanDialog):
        ScanDialog.setWindowTitle(_translate("ScanDialog", "Dialog", None))
        self.tipLabel.setText(_translate("ScanDialog", "TextLabel", None))
        self.cancelButton.setText(_translate("ScanDialog", "Cancel", None))

from widget.BLEListWidget import BLEListWidget
