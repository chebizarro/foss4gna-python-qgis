# -*- coding: utf-8 -*-
"""
/*************************************************************************
 WhereAmIDialog
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

from PyQt4 import QtCore, QtGui
from ui_whereami import Ui_WhereAmI
# create the dialog for zoom to point


class WhereAmIDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_WhereAmI()
        self.ui.setupUi(self)
        # attribute for storing the position of the dialog
        self.userPos = None

    def moveEvent(self, event):
        self.userPos = event.pos()
