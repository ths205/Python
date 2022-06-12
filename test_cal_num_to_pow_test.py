#Tests that the file cal_num_to_pow_n.py runs correctly
import cal_num_to_pow_n

import unittest

#import pytest

class Num_to_Pow(unittest.TestCase):
#n is exponent and x is integer
   def test_raise_type_error_n_is_string(self):
       #exponent is string instead of integer
       n="luigi"
       x=9
       self.assertRaises(TypeError,cal_num_to_pow_n.x_to_pow_n,x,n)

   def test_raise_type_error_x_is_string(self):
       x="luigi"
       n=4
       self.assertRaises(TypeError,cal_num_to_pow_n.x_to_pow_n,x,n)

   def test_raise_zero_error(self):
       x=0
       n=-1
       #self.assertRaises(ZeroDivisionError('You gave me a number x which is 0 and an exponent that is less than 0'),cal_num_to_pow_n.x_to_pow_n(x,n))
       self.assertRaises(ZeroDivisionError,cal_num_to_pow_n.x_to_pow_n,x,n)


   def test_exponent_is_zero(self):
   #n is the exponent
       n=0
       x=8
       self.assertEqual(1,cal_num_to_pow_n.x_to_pow_n(x,n))

   def test_exponent_only_is_negative(self):
       n=-1
       x=2
       self.assertEqual(0.5,cal_num_to_pow_n.x_to_pow_n(x,n))
         
if __name__== '__main__':
       unittest.main()         
