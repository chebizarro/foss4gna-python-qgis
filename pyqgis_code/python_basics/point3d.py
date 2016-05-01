from qgis.core import QgsPoint


class Point3D(QgsPoint):

    def __init__(self, x, y, z):
        super(Point3D, self).__init__(x, y)
        self.z_value = z

    def setZ(self, z):
        self.z_value = z

    def z(self):
        return self.z_value

    def toString(self):
        return u"{:.2f}, {:.2f}, {:.2f}".format(self.x(), self.y(), self.z())
