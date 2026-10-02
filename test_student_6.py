import pytest

@pytest.fixture
def marks():
    return [80,90,70]

def test_marks(marks):
    average = sum(marks) / len(marks)
    assert average == 80

def test_length(marks):
    length = len(marks)
    assert length == 3

def large(marks):
    lar = marks[0]
    for i in range(len(marks)):
        if lar < marks[i]:
            lar = marks[i]
    return lar

       
    

def test_largest_number(marks):
    largest = large(marks)
    print("largest is : ",largest)
    assert largest == 90