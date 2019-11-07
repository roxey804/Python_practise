import program
import pytest
from program import random_int



def test_addition():
    assert program.addition(2,3) == 5
    assert program.addition(5,5) == 10
    assert program.addition(2,-3) == -1
    print("addition passed") 

def test_subtraction():
    assert program.subtraction(3,2) == 1
    #assert program.addition(-2,-3) == -5
    print("subtraction passed") 
    
def test_division():
    assert program.division(2,2) == 1
    print("division passed") 

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0

def test_multiplication():
    assert program.multiplication(2) == 4

def test_random_int():
    assert type(program.random_int(2,6)) == int  #asserting types is not recommended in python
    assert program.random_int(2,6) <=6
    assert program.random_int(2,6) >=2 
 