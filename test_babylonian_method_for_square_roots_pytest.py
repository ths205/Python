#This program users pytest to test that the program babylonian_method_for_square_roots works correctly
import pytest
import babylonian_method_for_square_roots

def test_babylonian_find_square_root_zero_division_error():
    with pytest.raises(ZeroDivisionError):

    #tests if a user enters an integer that is 0
         x_0=0
         s= 9
         decimal_places = 2
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )

#Tests that ValueError is raised when initial guess is negative
def test_babylonian_find_square_root_when_x_0_is_negative():
    with pytest.raises(ValueError):

         x_0 = -1

         s = 3

         decimal_places =5
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )

#Tests that ValueError is raised when root is negative
def test_babylonian_find_square_root_when_root_is_negative():
    with pytest.raises(ValueError):

         x_0 = 1

         s = -3

         decimal_places =5
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )


#Tests that ValueError is raised when decimal places is negative
def test_babylonian_find_square_root_when_decimal_places_is_negative():
    with pytest.raises(ValueError):

         x_0 = 1

         s = 3

         decimal_places = -5
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )

#Tests that a type error is raised if a user inputs a string as a root
def test_babylonian_find_square_root_type_error_initial_guess_is_string():
    with pytest.raises(TypeError):
         x_0 ="tyr"
         s = 10
         decimal_places = 5
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )

#Tests that a type error is raised if a user inputs a string as a root
def test_babylonian_find_square_root_type_error_root_is_string():
    with pytest.raises(TypeError):
         x_0 = 4
         s = "tyr"
         decimal_places = 5
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )
         
#Tests that a type error is raised if a user inputs a string as a root
def test_babylonian_find_square_root_type_error_decimal_places_is_string():
    with pytest.raises(TypeError):
         x_0 = 4
         s = 9
         decimal_places = "tyr"
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )

#Tests to make sure user raises a TypeError if a char is given as input for an initial guess instead of a positive number
def test_babylonian_find_square_root_type_error_initial_guess_is_chr():
    with pytest.raises(TypeError):
         x_0 = 'i'
         s = 10
         decimal_places = 5
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )

#Tests to make sure user raises a TypeError if a char is given as input for a root instead of a positive number
def test_babylonian_find_square_root_type_error_root_is_chr():
    with pytest.raises(TypeError):
         x_0 = 4
         s = 'i'
         decimal_places = 5
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )

#Tests to make sure user raises a TypeError if a char is given as input for a number of decimal places instead of a positive number
def test_babylonian_find_square_root_type_error_decimal_places_is_chr():
    with pytest.raises(TypeError):
         x_0 = 4
         s = 10000
         decimal_places = 'i'
         babylonian_method_for_square_roots.babylonian_find_square_root(x_0, s, decimal_places )

    
def test_produces_correct_output():
         
    x_0 = 4
    root = 50965321
    decimal_places = 6
    assert babylonian_method_for_square_roots.babylonian_find_square_root(x_0,root,decimal_places) == 7139





