from without_fixtures_4 import calculate_total

#Yes — without a fixture, you usually **prepare the required setup/test data inside each test function again**, which can cause repetition across multiple tests.

def test_calculate_total():
    prices = [10,40,10] # we are repeating this one
    result = calculate_total(prices)

    assert result == 60