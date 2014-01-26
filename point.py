# point.py
# Walker M. White
# August 16, 2012
"""Module that provides a type for a point in 3D space

This module allows the user to create Point objects. It is not
important to understand the code in this module to do the
lab. All you need to know is that Point objects have three
attributes - x, y, and z - and no (significant) methods"""

class Point(object):
    """An instance is a point in 3D space"""

    @property
    def x(self):
        """x-coordinate; value is a float."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = float(value)

    @x.deleter
    def x(self):
        del self._x 

    @property
    def y(self):
        """y-coordinate; value is a float."""
        return self._y

    @y.setter
    def y(self, value):
        self._y = float(value)

    @y.deleter
    def y(self):
        del self._y     

    @property
    def z(self):
        """z-coordinate; value is a float."""
        return self._z

    @z.setter
    def z(self, value):
        self._z = float(value)

    @z.deleter
    def z(self):
        del self._z     

    # METHODS
    def __init__(self, x=0, y=0, z=0):
        """Constructor: Point (x,y,z). Values are 0 by default. """
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        """Returns: True if self and other are equivalent points. """
        return (type(other) == Point and self.x == other.x and 
                self.y == other.y and self.z == other.z)

    def __str__(self):
        """Returns: Readable String representation of this color. """
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def __repr__(self):
        """Returns: Unambiguous String representation of this color. """
        return "%s%s" % (self.__class__,self.__str__())
