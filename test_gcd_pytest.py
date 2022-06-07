#Import gcd to write  tests with pytest
import pytest

import gcd

#when x  is a string and y is an integer
def test_raise_type_error_x_is_string():
    with pytest.raises(TypeError):

         x = "sfbhsbkv"
         y = 6
         gcd.gcd(x,y)

#Test case when y is a string
def test_raise_type_error_when_y_is_string():
    with pytest.raises(TypeError):

         x= 10

         y = "fdkvf"

         gcd.gcd(x,y)

#Testcase for when x is a double
def test_raise_type_error_when_x_is_double():
    with pytest.raises(TypeError):

         x=6.7

         y = 0
         gcd.gcd(x,y)


#TestCase when y is double
def test_raise_type_error_when_y_is_double():
    with pytest.raises(TypeError):

         y=6.7

         x = 0
         gcd.gcd(x,y)

#TestCase when x is a float
def test_raise_type_error_when_x_is_float():
    with pytest.raises(TypeError):

         x = 3.14657655

         y = 2

         gcd.gcd(x,y)
        
#TestCase when y is a float
def test_raise_type_error_when_y_is_float():
    with pytest.raises(TypeError):

         y = 3.14657655

         x = 2

         gcd.gcd(x,y)

#TestCase when x is a negative value
def test_raise_value_error_when_x_is_negative_integer():
    with pytest.raises(ValueError):

         x = -5

         y = 5

         gcd.gcd(x,y)

def test_raise_value_error_when_y_is_negative_integer():
    with pytest.raises(ValueError):

         y = -5

         x = 5

         gcd.gcd(x,y)

def test_produces_correct_output():
    x = 36
    y = 60
    assert gcd.gcd(36,60) == 12        
