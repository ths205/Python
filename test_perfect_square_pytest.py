#This file uses pytest to test that the file perfect_square.py works as it should.
#To run this file type "pytest -s test_perfect_square_pytest.py"
import pytest
import perfect_square

#import pytest

def test_raise_value_error():
    with pytest.raises(ValueError):
    #tests if the user enters an integer that is less than 0
         x= -1
         perfect_square.perfect_square(x)

#tests if user enters a char such as 'A' instead of an integer
def test_raise_type_error_ch():
    with pytest.raises(TypeError):
         x = 'c'
         perfect_square.perfect_square(x)

#tests if user enters a string such as "thing#" instead of an integer
def test_raise_type_error_st():
    with pytest.raises(TypeError):
         x = "thing#"
         perfect_square.perfect_square(x)

#tests if user enters a double such as 3.14 instead of an integer
def test_raise_type_error_doub():
    with pytest.raises(TypeError):
         x = 3.14
         perfect_square.perfect_square(x)

#tests if user enters a float such as 3.14159265 instead of an integer
def test_raise_type_error_flt():
    with pytest.raises(TypeError):
         x = 3.14159265
         perfect_square.perfect_square(x)

#Tests if the file returns a perfect square if the user enters an integer that is
#suppose to return a perfect square
def test_it_is_a_perfect_square():
    x=1
    assert perfect_square.perfect_square(x)=="It is a perfect square"
#Tests if the file returns a  perfect square for  when a user enters 0
def test_it_is_a_perfect_square_zero():
    x=0
    assert perfect_square.perfect_square(x)=="It is a perfect square"

#Tests if the file does not returns a perfect square if the user enters an integer that is
#not suppose to return a perfect square
def test_it_is_not_a_perfect_square():
    x=3
    assert perfect_square.perfect_square(x)=="It is not a perfect square"
