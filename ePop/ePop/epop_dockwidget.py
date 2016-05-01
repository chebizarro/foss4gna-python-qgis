# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ePopDockWidget
                                 A QGIS plugin
 ePop
                             -------------------
        begin                : 2016-04-30
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Chris Daley
        email                : chebizarro@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
#from PyQt4.QtCore import pyqtSignal
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'epop_dockwidget_base.ui'))


class ePopDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, iface=None, parent=None):
        """Constructor."""
        super(ePopDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
	self.iface = iface
	#QObject.connect(self.pushButton, SIGNAL("clicked()"), self.zoom)
	self.pushButton.clicked.connect(self.zoom)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def zoom(self):
	self.iface.zoomFull()
