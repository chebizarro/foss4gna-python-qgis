import os

from PyQt4.QtGui import *

from qgis.gui import *
from qgis.core import *


class OurMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setupGui()

        self.add_ogr_layer('/data/alaska.shp')
        self.map_canvas.zoomToFullExtent()

    def setupGui(self):
        frame = QFrame(self)
        self.setCentralWidget(frame)
        self.grid_layout = QGridLayout(frame)

        self.map_canvas = QgsMapCanvas()
        self.map_canvas.setCanvasColor(QColor(255, 255, 255))
        self.grid_layout.addWidget(self.map_canvas)

    def add_ogr_layer(self, path):
        (name, ext) = os.path.basename(path).split('.')
        layer = QgsVectorLayer(path, name, 'ogr')
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        canvas_layer = QgsMapCanvasLayer(layer)
        self.map_canvas.setLayerSet([canvas_layer])
