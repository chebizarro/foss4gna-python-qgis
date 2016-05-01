# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WhereAmI
                                 A QGIS plugin
 Display coordinates of a map click
                             -------------------
        begin                : 2013-12-07
        copyright            : (C) 2014 by gsherman
        email                : gsherman@geoapt.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def classFactory(iface):
    # load WhereAmI class from file WhereAmI
    from whereami import WhereAmI
    return WhereAmI(iface)
