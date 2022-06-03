

#Writing testcases for the file gcd.py
#Please run through the command pytest test_gcd.py

import unittest

import gcd

class GCD_Test(unittest.TestCase):

#TestCase when  x is string and y is integer
   def test_raise_type_error_when_x_is_string(self):

       x = "sfbhsbkv"

       y =  6

       self.assertRaises(TypeError, gcd.gcd,x,y)

#TestCase for y is a string
   def test_raise_type_error_when_y_is_string(self):

       x = 10

       y=  "fdkvf"

       self.assertRaises(TypeError, gcd.gcd,x,y)

#TestCase for x is  a double
   def test_raise_type_error_when_x_is_double(self):

       x=6.7

       y = 0

       self.assertRaises(TypeError, gcd.gcd, x, y)

#TestCase when y is a double
   def test_raise_type_error_when_y_is_double(self):

       x=1

       y = 6.7

       self.assertRaises(TypeError, gcd.gcd, x, y)

#TestCase when x is a float
   def test_raise_type_error_when_x_is_a_float(self):

       x = 3.14657655

       y = 2

       self.assertRaises(TypeError, gcd.gcd, x, y)

#TestCase when y is a float
   def test_raise_type_error_when_y_is_a_float(self):

       y = 3.14657655

       x = 2

       self.assertRaises(TypeError, gcd.gcd, x, y)

#TestCase when x is a negative value
   def  test_raise_value_error_when_x_is_negative_integer(self):

       x = -5

       y = 5

       self.assertRaises(ValueError, gcd.gcd, x, y)

#TestCase when y is a negative value
   def  test_raise_value_error_when_x_is_negative_integer(self):

       x = 5

       y = -5

       self.assertRaises(ValueError, gcd.gcd, x, y)

#TestCase that method gcd produces the  correct output

   def  test_produces_correct_output(self):

       x  = 36

       y = 60

       self.assertEqual(12,gcd.gcd(x,y))
