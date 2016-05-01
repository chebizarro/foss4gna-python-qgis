from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
from qgis.utils import iface


def load_layer():
    wb = QgsVectorLayer('/data/world_borders.shp', 'world_borders', 'ogr')
    QgsMapLayerRegistry.instance().addMapLayer(wb)


def change_color():
    active_layer = iface.activeLayer()
    renderer = active_layer.rendererV2()
    symbol = renderer.symbol()
    symbol.setColor(QColor(Qt.red))
    iface.mapCanvas().refresh()
    iface.legendInterface().refreshLayerSymbology(active_layer)


def open_attribute_table():
    iface.showAttributeTable(iface.activeLayer())
