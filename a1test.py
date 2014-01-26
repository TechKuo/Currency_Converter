#a1test.py
#Charles Lai and Tech Kuo cjl223 thk43
#9/15/2012
"""Unit test for module a1

When run as an application, this module invokes several 
procedures that test the various functions in the module 
a1."""

import cunittest
from a1 import *

def testA():
    #This function tests the functions before_space() and after_space()
    s = "before after"
    r = before_space(s)
    t = after_space(s)
    cunittest.assert_equals("before",r)
    cunittest.assert_equals("after",t)
    
    s = "123456 currency name"
    r = before_space(s)
    t = after_space(s)
    cunittest.assert_equals("123456",r)
    cunittest.assert_equals("currency name",t)
    
    s = "before    after"
    r = before_space(s)
    t = after_space(s)
    cunittest.assert_equals("before",r)
    cunittest.assert_equals("   after",t)
    
    s = " after"
    r = before_space(s)
    t = after_space(s)
    cunittest.assert_equals("",r)
    cunittest.assert_equals("after",t)

def testB():
    #This function tests the functions get_lhs() and get_rhs() as well as first_inside_quotes()
    query = '{lhs: "2.5 U.S. dollars",rhs: "2.0366598775 Euros",error: "",icc: true}'
    g = get_lhs(query)
    r = get_rhs(query)
    cunittest.assert_equals('2.5 U.S. dollars',g)
    cunittest.assert_equals('2.0366598775 Euros',r)
    
    query = '{lhs: "500 U.S. dollars",rhs: "39578.8807 Japanese yen",error: "",icc: true}'
    g = get_lhs(query)
    r = get_rhs(query)
    cunittest.assert_equals('500 U.S. dollars',g)
    cunittest.assert_equals('39578.8807 Japanese yen',r)
    
    query = '{lhs: "",rhs: "",error: "4",icc: false}'
    g = get_lhs(query)
    r = get_rhs(query)
    cunittest.assert_equals('',g)
    cunittest.assert_equals('',r)
    
    #This is a test case for first_inside_quotes() only
    s = 'The string "over nine thousand" is in the middle'
    t=first_inside_quotes(s)
    cunittest.assert_equals("over nine thousand",t)

def testC():
    #This function tests the function currency_repsponse()
    answer = currency_response(2.5, 'USD', 'EUR')
    cunittest.assert_equals('{lhs: "2.5 U.S. dollars",rhs: "2.0366598775 Euros",error: "",icc: true}',answer)
    
    answer = currency_response(800, 'CNY', 'TWD')
    cunittest.assert_equals('{lhs: "800 Chinese yuan",rhs: "3768.542893112 Taiwan dollars",error: "",icc: true}',answer)

    answer = currency_response(2.5, 'MERICA', 'SOVIETS')
    cunittest.assert_equals('{lhs: "",rhs: "",error: "4",icc: false}',answer)

def testD():
    #This function tests the functions iscurrency() and exchange()
    #These three test cases are for iscurrency()
    r = iscurrency("JPY")
    cunittest.assert_equals(True,r)
    r = iscurrency("UST")
    cunittest.assert_equals(False,r)
    r = iscurrency("Z Z")
    cunittest.assert_equals(False,r)
    #These three test cases are for exchange()
    r = exchange(100, "USD", "EUR")
    cunittest.assert_floats_equal(81.4663951,r)
    r = exchange(867.589, "CNY", "TWD")
    cunittest.assert_floats_equal(4086.9329501151,r)
    r = exchange(200, "JPY", "JPY")
    cunittest.assert_floats_equal(200,r)
    
    
if __name__ == "__main__":
    testA()
    testB()
    testC()
    testD()
    print "Module a1 is working correctly"