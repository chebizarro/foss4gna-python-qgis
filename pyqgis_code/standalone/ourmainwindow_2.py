import os

from PyQt4.QtGui import *

from qgis.gui import *
from qgis.core import *

import resources


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

        # setup action(s)
        self.zoomin_action = QAction(
            QIcon(":/ourapp/zoomin_icon"),
            "Zoom In",
            self)
        # create toolbar
        self.toolbar = self.addToolBar("Map Tools")
        self.toolbar.addAction(self.zoomin_action)

        # connect the tool(s)
        self.zoomin_action.triggered.connect(self.zoom_in)

        # create the map tool(s)
        self.tool_zoomin = QgsMapToolZoom(self.map_canvas, False)

    def add_ogr_layer(self, path):
        (name, ext) = os.path.basename(path).split('.')
        layer = QgsVectorLayer(path, name, 'ogr')
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        canvas_layer = QgsMapCanvasLayer(layer)
        self.map_canvas.setLayerSet([canvas_layer])

    def zoom_in(self):
        self.map_canvas.setMapTool(self.tool_zoomin)
