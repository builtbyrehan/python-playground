import pytest
from parametrised_test_2 import square

@pytest.mark.parametrize(
    "num,expected",[(2,4),(3,9),(4,16),(5,25)]
)
def test_square_function(num,expected):
    assert square(num) == expected