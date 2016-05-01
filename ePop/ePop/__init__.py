# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ePop
                                 A QGIS plugin
 ePop
                             -------------------
        begin                : 2016-04-30
        copyright            : (C) 2016 by Chris Daley
        email                : chebizarro@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ePop class from file ePop.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .epop import ePop
    return ePop(iface)
