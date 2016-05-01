# -*- coding: utf-8 -*-
"""
/***************************************************************************
 libePop
                                 A QGIS plugin
 libePop
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

import processing

class libePop:

	def make_grid(self, layer):
		
		processing.runalg('qgis:creategird', 1, width, height, hspacing,
			vspacing, centerx, centery, crs, output)
		
