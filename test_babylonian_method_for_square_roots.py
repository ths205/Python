#This program tests that the babylonian_method_for_square_roots.py program for calculating square roots works correctly
import unittest

import babylonian_method_for_square_roots

class Babylonian_Method_Test(unittest.TestCase):
    
    #Tests to make sure a Division by zero error is raised when a user makes the intial guess 0
    def test_babylonian_find_square_root_divide_by_zero_initial_guess(self):
        #initialguess
         x_0=0
        #wanting the square root of
         root = 100
        #number of decimal places
         d =3
         
         self.assertRaises(ZeroDivisionError,babylonian_method_for_square_roots.babylonian_find_square_root,x_0,root,d)
    
    #Tests that a ValueError is raised when a user makes the initial guess a negative number
    def test_babylonian_find_square_root_value_error_when_x_0_is_negative(self):
        #initial guess
        x_0 = -1
        #number to get the square root of
        root = 3
        #number of decimal places
        d=5
        
        self.assertRaises(ValueError,babylonian_method_for_square_roots.babylonian_find_square_root,x_0,root,d)
    
    #Tests to make sure that a ValueError is raised when the user types in a negative number that we want to get the square root of.
    def test_babylonian_find_square_root_value_error_when_root_is_negative(self):
        #initial guess
        x_0 = 1
        #number to get the square root of
        root = -3
        #number of decimal places
        d=5
        
        self.assertRaises(ValueError,babylonian_method_for_square_roots.babylonian_find_square_root,x_0,root,d)
    
    #Test to make sure that a ValueError is raised when the user types in a negative number that we want to get the number of decimal places for
    def test_babylonian_find_square_root_value_error_when_decimal_is_negative(self):
        #initial guess
        x_0 = 1
        #number to get the square root of
        root = 3
        #number of decimal places
        d=-5
        
        self.assertRaises(ValueError,babylonian_method_for_square_roots.babylonian_find_square_root,x_0,root,d)
    
    #Tests to make sure the program produces the almost correct result for the square root of 50965321
    def test_babylonian_find_square_root(self):
        #initial guess
        x_0 = 2
        #number to get the square root of
        root = 50965321
        d = 3
        
        self.assertAlmostEqual(7139.0, babylonian_method_for_square_roots.babylonian_find_square_root(x_0,root,d) )

if __name__ =='__main__':
        unittest.main()
