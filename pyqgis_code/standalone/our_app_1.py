from PyQt4.QtGui import *
from qgis.core import *

from ourmainwindow import OurMainWindow

app = QApplication([])
# set up QGIS
QgsApplication.setPrefixPath('/dev1/apps/qgis', True)
QgsApplication.initQgis()

# set the main window and show it
mw = OurMainWindow()
mw.show()

app.exec_()

# "delete" our main window
mw = None
# clean up QGIS
QgsApplication.exitQgis()
