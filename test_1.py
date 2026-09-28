
import pytest
from pytest_1 import add,mul,div,sub
# test goes here for add function
def test_add():
    assert add(2,3) == 5

def test_sub(): 
    assert sub(3,2) == 1 

def test_mul():
    assert mul(2,3)  == 6

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)
