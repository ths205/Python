#Using Pytest to test to make sure sub_factorial.py file  works correctly
#Run the file by typing "pytest test_sub_factorial_pytest.py"
         
import pytest
         
import sub_factorial

#The first  3  test  cases  test  if the user enters inapprpriate input
def test_raise_type_error_input_is_string():
    with pytest.raises(TypeError):

         x = "sfbhsbkv"
         sub_factorial.factorial_sub(x)
    
def test_raise_type_error_when_x_is_double():
     with pytest.raises(TypeError):
         x= 5.9
         sub_factorial.factorial_sub(x)


def test_raise_type_error_when_y_is_float():
    with pytest.raises(TypeError):
          
          y = 3.14657655
          sub_factorial.factorial_sub(y)

#tests for when the user enters negative input
def test_raise_value_error_when_y_is_negative_integer():
    with pytest.raises(ValueError):
          y= -1
          sub_factorial.factorial_sub(y)
         
#Tests for the case for when the  input  is one  
def test_produces_correct_output_if_x_is_one():
         x= 1
         assert sub_factorial.factorial_sub(x)==0
         
#Tests for the case for when the  input  is two
def test_produces_correct_output_if_x_is_two():
         x= 2
         assert sub_factorial.factorial_sub(x)==1

#Tests for the case for when the  input  is four
def test_produces_correct_output_if_x_is_two():
         x= 4
         assert sub_factorial.factorial_sub(x) == 9
