from with_fixture_5 import calculate_total

import pytest

@pytest.fixture
def prices():
    price = [1,2,3]
    return price

def test_calculate_total(prices):
    # now we have no need to again define the sample data here for testing purpose
    result = calculate_total(prices)
    assert result == 6