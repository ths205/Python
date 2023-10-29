#Tests that the file perfect_square.py works as it should
import perfect_square

import unittest

class Test_Perfect_Square(unittest.TestCase):

    def test_raise_value_error(self):
        #tests to  make sure  that the program does not  accept negative integers
        self.assertRaises(ValueError,perfect_square.perfect_square,-1)

    def test_raise_type_error_ch(self):
        #tests to make sure that the program doesnot  accept  character values
        self.assertRaises(TypeError, perfect_square.perfect_square,'c')

    def test_raise_type_error_st(self):
        #tests to make sure that the program doesnot  accept  string values
        self.assertRaises(TypeError, perfect_square.perfect_square,"string#")

    def test_raise_type_error_doub(self):
        #tests to make sure that the program doesnot  accept  double values
        self.assertRaises(TypeError, perfect_square.perfect_square,3.14)


    def test_raise_type_error_flt(self):
        #tests to make sure that the program doesnot  accept  double values
        self.assertRaises(TypeError, perfect_square.perfect_square,3.14159265)

    def test_assert_not_perfect_square(self):
        self.assertEqual("It is not a perfect square",perfect_square.perfect_square(3))

    def test_assert_perfect_square_equal(self):
        self.assertEqual("It is a perfect square",perfect_square.perfect_square(1))

if __name__== '__main__':
   unittest.main()
