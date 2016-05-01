class Point:
    """ Class to model a point in 2D space."""

    """ Size of our marker in pixels """
    marker_size = 4

    def draw(self):
        """Draw the point on the map canvas"""
        print "drawing the point"

    def move(self, new_x, new_y):
        """ Move the point to a new location on the
            map canvas"""
        print "moving the point"
