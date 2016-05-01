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

from qgis.gui import QgsMessageBar

import processing

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'epop_dockwidget_base.ui'))


class ePopDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, iface, parent=None):
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
	self.addGridButton.clicked.connect(self.addGrid)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def addGrid(self):
	layer = self.iface.activeLayer()
	if layer is None:
		self.iface.messageBar().pushMessage("Error",
			"You must select a feature",
			level=QgsMessageBar.CRITICAL,
			duration=3)
		return
	
	if len(layer.selectedFeatures()) < 1:
		self.iface.messageBar().pushMessage("Error",
			"You must select a feature",
			level=QgsMessageBar.CRITICAL,
			duration=3)
	elif len(layer.selectedFeatures()) > 1:
		self.iface.messageBar().pushMessage("Error",
			"You must select only one feature",
			level=QgsMessageBar.CRITICAL,
			duration=3)
	else:
		feature = layer.selectedFeatures()[0]
		bbox = feature.geometry().boundingBox()
		extent = "%d,%d,%d,%d" % (bbox.xMinimum(), bbox.xMaximum(),
			bbox.yMinimum(), bbox.yMaximum())
		
		processing.runalg('qgis:creategrid', 1, extent,
			0.00025, 0.00025,'EPSG:4326','/tmp/tmp.shp')
