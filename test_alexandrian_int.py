#This program tests the python file alexandrian_integers.py
import alexandrian_integers

import unittest

class Test_Alex_Int(unittest.TestCase):

   def test_raise_type_error_case_p(self):

       self.assertRaises(TypeError, alexandrian_integers.alex_integer,1,'s',3,4)

   def test_raise_type_error_case_a(self):

       self.assertRaises(TypeError, alexandrian_integers.alex_integer,'s',1,3,4)

   def test_raise_type_error_case_q(self):

       self.assertRaises(TypeError,alexandrian_integers.alex_integer,1,3,'s',4)

   def test_raise_type_error_case_r(self):

       self.assertRaises(TypeError,alexandrian_integers.alex_integer,1,3,4,'s')

   def test_raise_zero_division_error_case_p(self):

       self.assertRaises(ZeroDivisionError, alexandrian_integers.alex_integer,1,0,4,5)

   def test_raise_zero_division_error_case_a(self):

       self.assertRaises(ZeroDivisionError, alexandrian_integers.alex_integer,0,1,4,5)

   def test_raise_zero_division_error_case_q(self):

       self.assertRaises(ZeroDivisionError, alexandrian_integers.alex_integer,1,4,0,5)

   def test_raise_zero_division_error_case_r(self):

       self.assertRaises(ZeroDivisionError, alexandrian_integers.alex_integer,1,4,5,0)


   def test_alex_integer(self):

       self.assertEqual(str(630)+ " is an Alexandrian Integer", alexandrian_integers.alex_integer(630,5,7,18) )

if __name__ =='__main__':
       unittest.main()
