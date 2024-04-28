import pytest
import alexandrian_integers
    
def test_raise_division_by_zero_error_with_x():
    with pytest.raises(ZeroDivisionError):
            
         x=0
         y=2
         z=3
         v=4
         alexandrian_integers.alex_integer(x, y, z, v)
    
def test_raise_division_by_zero_error_with_y():
    with pytest.raises(ZeroDivisionError):
            
         x=2
         y=0
         z=3
         v=4
         alexandrian_integers.alex_integer(x, y, z, v)
    
def test_raise_division_by_zero_error_with_z():
    with pytest.raises(ZeroDivisionError):
                
         x=3
         y=2
         z=0
         v=4
         alexandrian_integers.alex_integer(x, y, z, v)
    
def test_raise_division_by_zero_error_with_v():
    with pytest.raises(ZeroDivisionError):
            
         x=4
         y=2
         z=3
         v=0
         alexandrian_integers.alex_integer(x, y, z, v)
    
def test_raise_type_error_x_is_chr():
    with pytest.raises(TypeError):
            
         x='c'
         y=3
         z=2
         v=5
         alexandrian_integers.alex_integer(x,y,z,v)

def test_raise_type_error_y_is_chr():
    with pytest.raises(TypeError):
            
         x=3
         y='c'
         z=2
         v=5
         alexandrian_integers.alex_integer(x,y,z,v)

def test_raise_type_error_z_is_chr():
    with pytest.raises(TypeError):
            
         x=2
         y=3
         z='c'
         v=5
         alexandrian_integers.alex_integer(x,y,z,v)

    
def test_raise_type_error_v_is_chr():
    with pytest.raises(TypeError):
            
         x=5
         y=3
         z=2
         v='c'
         alexandrian_integers.alex_integer(x,y,z,v)
    
def test_raise_type_error_x_is_str():
    with pytest.raises(TypeError):
         
         x="xyz"
         y=3
         z=2
         v=5
         alexandrian_integers.alex_integer(x,y,z,v)

def test_raise_type_error_y_is_str():   
    with pytest.raises(TypeError):
              
         x=3
         y="xyz"
         z=2
         v=5  
         alexandrian_integers.alex_integer(x,y,z,v)

def test_raise_type_error_z_is_str():   
    with pytest.raises(TypeError):
            
         x=2
         y=3
         z="xyz"
         v=5
         alexandrian_integers.alex_integer(x,y,z,v)

def test_raise_type_error_v_is_str():   
    with pytest.raises(TypeError):
            
         x=5
         y=3  
         z=2
         v="xyz"
         alexandrian_integers.alex_integer(x,y,z,v)

def test_raise_type_error_v_is_double():
    with pytest.raises(TypeError):
            
         x=5
         y=3
         z=2  
         v=2.5
         alexandrian_integers.alex_integer(x,y,z,v)

def test_raise_type_error_z_is_double():
    with pytest.raises(TypeError):
            
         x=5
         y=3
         z=2.5
         v=2
         alexandrian_integers.alex_integer(x,y,z,v)

def test_raise_type_error_y_is_double():
    with pytest.raises(TypeError):
            
         x=5  
         y=3.0
         z=2
         v=2
         alexandrian_integers.alex_integer(x,y,z,v)

def test_raise_type_error_x_is_double():
    with pytest.raises(TypeError):
              
         x=5.0
         y=3  
         z=2  
         v=2
         alexandrian_integers.alex_integer(x,y,z,v)
