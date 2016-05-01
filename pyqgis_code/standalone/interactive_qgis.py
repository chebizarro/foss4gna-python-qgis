from PyQt4 import QtGui
from qgis.gui import *
from qgis.core import *

app = QtGui.QApplication([])
QgsApplication.setPrefixPath("/dev1/apps/qgis", True)
QgsApplication.initQgis()

main_win = QtGui.QMainWindow()
frame = QtGui.QFrame(main_win)
main_win.setCentralWidget(frame)
grid_layout = QtGui.QGridLayout(frame)

map_canvas = QgsMapCanvas()
grid_layout.addWidget(map_canvas)
map_canvas.setCanvasColor(QtGui.QColor(255, 255, 255))
layer = QgsVectorLayer(
    '/dev1/gis_data/qgis_sample_data/shapefiles/alaska.shp',
    'alaska',
    'ogr')
QgsMapLayerRegistry.instance().addMapLayer(layer)
canvas_layer = QgsMapCanvasLayer(layer)
map_canvas.setLayerSet([canvas_layer])
map_canvas.zoomToFullExtent()

main_win.show()

# Need the following statement if running as a script
app.exec_()
