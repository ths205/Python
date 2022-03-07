#Import the  cal_num_to_pow_n to write  tests with pytest
import pytest

import cal_num_to_pow_n

#n is exponent and x is integer
def test_raise_type_error_n_is_string():
    with pytest.raises(TypeError):
         n="luigi"
         x=9
         cal_num_to_pow_n.x_to_pow_n(x,n)

def test_raise_type_error_x_is_string():
    with pytest.raises(TypeError):
         x="luigi"
         n=4
         cal_num_to_pow_n.x_to_pow_n(x,n)

def test_raises_zero_error():
    with pytest.raises(ZeroDivisionError):
         x=0
         n=-1
         cal_num_to_pow_n.x_to_pow_n(x,n)
