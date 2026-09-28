import pytest
from parametrised_test_3 import is_even

@pytest.mark.parametrize("num,expected",[(1,False),(2,True),(-3,False),(10,True)])

def test_even_numbers(num,expected):
    assert is_even(num) == expected