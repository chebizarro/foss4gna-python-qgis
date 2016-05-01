# -*- coding: utf-8 -*-
"""
/**************************************************************************
 WhereAmI
                                 A QGIS plugin
 Display coordinates of a map click
                              -------------------
        begin                : 2013-12-07
        copyright            : (C) 2014 by gsherman
        email                : gsherman@geoapt.com
 *************************************************************************/

/*************************************************************************
 *                                                                       *
 *  This program is free software; you can redistribute it and/or modify *
 *  it under the terms of the GNU General Public License as published by *
 *  the Free Software Foundation; either version 2 of the License, or    *
 *  (at your option) any later version.                                  *
 *                                                                       *
 *************************************************************************/
"""
import os
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import QgsMapToolEmitPoint
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from whereamidialog import WhereAmIDialog


class WhereAmI:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # Create the dialog and keep reference
        self.dlg = WhereAmIDialog()
        # initialize plugin directory
        self.plugin_dir = os.path.join(
            QFileInfo(QgsApplication.qgisUserDbFilePath()).path(),
            "/python/plugins/whereami")

        # Store reference to the map canvas
        self.canvas = self.iface.mapCanvas()
        # Create the map tool using the canvas reference
        self.pointTool = QgsMapToolEmitPoint(self.canvas)

        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale")[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/whereami_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/whereami/whereami_icon.png"),
            u"Where Am I?", self.iface.mainWindow(),
            toolTip='Show me where I am',
            triggered=self.run)
        # connect signal that the canvas was clicked
        self.pointTool.canvasClicked.connect(self.display_point)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Where Am I?", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Where Am I?", self.action)
        self.iface.removeToolBarIcon(self.action)

    def display_point(self, point, button):
        # report map coordinates from a canvas click
        self.dlg.hide()
        coords = "{}, {}".format(point.x(), point.y())
        self.dlg.ui.lineEdit.setText(str(coords))
        # show the dialog
        if self.dlg.userPos is not None:
            self.dlg.move(self.dlg.userPos)
        self.dlg.show()

    # run method that performs all the real work
    def run(self):
        # set the map tool
        self.canvas.setMapTool(self.pointTool)
