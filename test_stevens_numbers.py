
#This file tests that the peterson_number python file works correctly. A peterson number is a number
#where the sum of the factorial of its integers adds to itself.
import peterson_number

import unittest

class Test_Peterson_Num(unittest.TestCase):
        
    def test_raise_typee_error_case_character(self):
    
        self.assertRaises(TypeError,peterson_number,'s')

    def test_raise_typee_error_case_negative_number(self):
       
        self.assertRaises(TypeError,peterson_number, -5)

    def test_peterson_num_true(self):
        self.assertEqual(str(145) +" is a Peterson number.", peterson_number.peterson_num(['1','4','5'], 145))

    def test_peterson_num_false(self):
        self.assertEqual(str(100) +" is not a Peterson number.",  peterson_number.peterson_num(['1','0','0'], 100) )

if __name__ =='__main__':
        unittest.main()
