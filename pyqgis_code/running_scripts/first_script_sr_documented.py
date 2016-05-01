"""FirstScript: A simple class used to load a layer in QGIS
and change its color."""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *


class FirstScript:
    """Class to load and render the world_borders shapefile."""

    def __init__(self, iface):
        self.iface = iface

    def load_layer(self):
        """Load the world_borders shapefile and add it to the map."""
        wb = QgsVectorLayer('/data/world_borders.shp', 'world_borders', 'ogr')
        QgsMapLayerRegistry.instance().addMapLayer(wb)

    def change_color(self):
        """Change the color of the active layer to red and update
        the legend."""
        active_layer = self.iface.activeLayer()
        renderer = active_layer.rendererV2()
        symbol = renderer.symbol()
        symbol.setColor(QColor(Qt.red))
        self.iface.mapCanvas().refresh()
        print "Version int: %i" % QGis.QGIS_VERSION_INT
        if QGis.QGIS_VERSION_INT < 10900:
            self.iface.refreshLegend(active_layer)
        else:
            self.iface.legendInterface().refreshLayerSymbology(active_layer)

    def open_attribute_table(self):
        """Open the attribute table for the active layer."""
        self.iface.showAttributeTable(self.iface.activeLayer())


def run_script(iface):
    """Run the script by instantiating FirstScript and calling
    methods."""
    print "creating object"
    fs = FirstScript(iface)
    print "loading layer"
    fs.load_layer()
    print "changing color"
    fs.change_color()
    print "opening attribute table"
    fs.open_attribute_table()
