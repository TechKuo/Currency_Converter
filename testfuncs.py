# testfuncs.py
# Tech Kuo
# September 12, 2012
"""Unit test to test the module pointfuncs.py"""
import cunittest          # For assert_equals and assert_true
from pointfuncs import *  # This is what we are testing
from point import *       # pointfuncs needs point to work

def test_has_a_zero():
    p=Point(0,1,1)
    result=has_a_zero(p)
    cunittest.assert_true(result)
    a=Point(1,1,1)
    result=has_a_zero(a)
    cunittest.assert_true(not result)
    b=Point(1,0,1)
    result=has_a_zero(b)
    cunittest.assert_true(result)
    c=Point(0,0,1)
    result=has_a_zero(c)
    cunittest.assert_true(result)

def test_shift():
    p=Point(1,2,3)
    shift(p)
    cunittest.assert_equals(2,p.x)
    cunittest.assert_equals(3,p.y)
    cunittest.assert_equals(1,p.z)
    
def test_parse():
    p=parse("(1,2,3)")
    cunittest.assert_equals(1,p.x)
    cunittest.assert_equals(2,p.y)
    cunittest.assert_equals(3,p.z)
    
def test_first_inside_quotes():
    s='The phrase I am trying to extract is "Hello World"'
    substring=first_inside_quotes(s)
    cunittest.assert_equals("Hello World",substring)
    
# Application code
if __name__ == "__main__":
    test_has_a_zero()
    test_shift()
    test_parse()
    test_first_inside_quotes()
    print "Module pointfuncs is working correctly"
    
