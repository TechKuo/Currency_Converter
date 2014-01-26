#a1.py
#Charles Lai and Tech Kuo cjl223 thk43
#9/15/2012
"""Module for currency exchange

This module provides several String parsing functions to 
implement a simple currency exchange routine using an 
online currency service. The primary function in this 
module is exchange()."""

from urllib2 import *

def exchange(amount_from, currency_from, currency_to):
    """Returns: amount of currency received in the given exchange.
    
    In this exchange, the user is changing <amount_from> money in 
    currency <currency_from> to the currency <currency_to>. 
    The value returned is a float representing the amount in 
    currency <currencyTo>
    
    Precondition: <amount_from> is a float. Both <currency_from> 
    and <currency_to> are strings with valid three-letter currency 
    codes."""

def before_space(s):
    """Returns: Substring of <s> up to, but not including, the first space of the string.
    
    Precondition: <s> has at least one space in it """
    
    the_space = s.find(" ")
    before = s[0:the_space]
    return before
    
    
def after_space(s):
    """ Returns: Substring of <s> after the first space
    
    Precondition: <s> has at least one space in it """
    
    the_space = s.find(" ")
    after = s[the_space+1:]
    return after

def first_inside_quotes(s):

    """Returns: The first substring of s between two (double) quote characters
    
    A quote character is one that is inside a string, not one that delimits it. Often we use \" to distinguish this from ".
    
    Example: If s is "A \"B C\" D", this function returns "B C"
    Example: If s is "A \"B C\" D \"E F\" G", this function still returns "B C" because it only picks the first such substring.
    
    Precondition: <s> is a string with at least two (double) quote characters inside."""

    first_quote = s.find('"')
    inner = s[first_quote+1:s.find('"',first_quote+1)]
    return inner

def get_lhs(query):

    """Returns: The LHS value in the response to a currency query.
    
    Given a JSON response to a currency query, this returns the string inside quotes (\") immediately following the keyword lhs. For example, if the JSON is
    
      "{lhs: \"2 U.S. dollars\",rhs: \"1.629327902 Euros\",error: \"\",icc: true}"
    
    then this function returns "2 U.S. dollars" (not "\"2 U.S. dollars\""). It returns the empty string if the JSON is the result of on invalid query.
    
    Precondition: <query> is the response to a currency query"""

    lhs = query.find("lhs")
    s = query[lhs:]
    currency_from = first_inside_quotes(s)
    return currency_from

def get_rhs(query):

    """Returns: The RHS value in the response to a currency query.
    
    Given a JSON response to a currency query, this returns the string inside quotes (\") immediately following the keyword rhs. For example, if the JSON is
    
      "{lhs: \"2 U.S. dollars\",rhs: \"1.629327902 Euros\",error: \"\",icc: true}"
    
    then this function returns "1.629327902 Euros" (not "\"1.629327902 Euros\""). It returns the empty string if the JSON is the result of on invalid query.
    
    Precondition: <query> is the response to a currency query """

    rhs = query.find("rhs")
    s = query[rhs:]
    currency_target = first_inside_quotes(s)
    return currency_target

def currency_response(amount_from, currency_from, currency_to):

    """Returns: A JSON string that is a response to a currency query.

    A currency query converts <amount_from> money in currency <currency_from> to the currency <currency_to>. The response should be a string of the form

      "{lhs: \"<old-amount>\",rhs: \"<new-amount>\",error: \"\",icc: true}"

    where the values <old-amount> and <new-amount> contain the value and name for the original and new currencies. If the query is invalid, both <old-amount> and <new-amount> will be empty.

    Precondition: <amount_from> is of type float, while <currency_from> and <currency_to> are of type string of valid code names for currency in capital letters """

    url = urlopen('http://cs1110.cs.cornell.edu/a1/calculator.php?q='+`amount_from`+currency_from+"=?"+currency_to)
    return url.read()

def iscurrency(currency):

    """Returns: True if <currency> is a valid (3 letter code for a) currency.

    Precondition: <currency> is a string."""
    
    c = currency_response(1, currency, currency)
    if c == '{lhs: "",rhs: "",error: "4",icc: false}':
        return False
    else:
        return True
        
def exchange(amount_from, currency_from, currency_to):

    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing <amount_from> money in currency <currency_from> to the currency <currency_to>. The value returned is a float representing the amount in currency <currencyTo>

    Precondition: <amount_from> is a float. Both <currency_from> and <currency_to> are strings with valid three-letter currency codes."""
    
    JSON = currency_response(amount_from, currency_from, currency_to)
    currency_target = get_rhs(JSON)
    currency_amount = before_space(currency_target)
    return float(currency_amount)







