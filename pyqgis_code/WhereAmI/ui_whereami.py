# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_whereami.ui'
#
# Created: Thu Jan  3 15:21:52 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WhereAmI(object):
    def setupUi(self, WhereAmI):
        WhereAmI.setObjectName(_fromUtf8("WhereAmI"))
        WhereAmI.resize(385, 116)
        self.label = QtGui.QLabel(WhereAmI)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(WhereAmI)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 341, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(WhereAmI)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 114, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(WhereAmI)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("pressed()")), WhereAmI.reject)
        QtCore.QMetaObject.connectSlotsByName(WhereAmI)

    def retranslateUi(self, WhereAmI):
        WhereAmI.setWindowTitle(QtGui.QApplication.translate("WhereAmI", "WhereAmI", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WhereAmI", "Coordinates of map click:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("WhereAmI", "Close", None, QtGui.QApplication.UnicodeUTF8))

