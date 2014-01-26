# pointfuncs.py
# Walker M. White
# August 16, 2012
"""Functions for handling Point objects

This module is kept separate from the module point.py for purposes
of readability.  While you do not know enough Python to understand
point.py yet, this module is fairly straightforward."""
from point import Point       # include Point in the active namespace
import math

def has_a_zero(p):
    """Returns: True if at least one of the coordinates of <p> is 0
    
    Precondition: <p> is a Point object"""
    return p.x == 0 or p.y == 0 or p.z == 0


def shift(p):
    """Shift the coordinates of p, so each coordinate moves 'left'
    
    The y-coordinate becomes the new x-coordinate,
    the z-coordinate becomes the new y-coordinate,
    and the x-coordinate becomes the new z-coordinate.
    For example, (1,2,3) becomes (2,3,1).
    
    Precondition: <p> is a Point object"""
    x = p.x
    p.x = p.y
    p.y = p.z
    p.z = x
    


def parse(s):
    """Returns: a point object whose representation is the string <s>
    
    Given a string such as "(1,2.2,3)", this function returns a point
    object equivalent to it. It uses find() and string slicing to
    break the string up into individual parts. It then converts the
    three coordinates in the string to floats, and puts them inside
    a point object.
    
    Precondition: <s> is a string representing a Point object"""
    # Find the first comma
    first = s.find(",")
    
    # x coordinate is between paren and first comma
    xstring = s[1:first]
    
    # Get the slice after the first comma
    after_comma = s[first+1:]
    
    # Use new slice to find the second comma
    second = after_comma.find(",")
    
    # Use second comma to get x and y coordinates
    # REMEMBER: Working with aftercomma, not s!!
    ystring = after_comma[0:second]
    zstring = after_comma[second+1:len(after_comma)-1]
    

    # Create a new point object
    p = Point()
    
    # Convert coordinates to points and put them in object
    p.x = float(xstring)
    p.y = float(ystring)
    p.z = float(zstring)

    # All done
    return p


def first_inside_quotes(s):
    """ Returns: The first substring of s between two (double) quote characters
    Example: If s is "A \"B C\" D", this function returns "B C"
    Example: If s is "A \"B C\" D \"E F\" G", this function still returns "B C"
    because it only picks the first such substring.

 Precondition: <s> is a string with at least two (double) quote characters inside"""
 
    q = s.find('"')                #Finds the first quotation mark and stores location in q
    inner=s[q+1:s.find('"',q+1)]   #Slices the string into the substring between quotes
    return inner
 