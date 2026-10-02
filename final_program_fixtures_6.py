'''

Create a small Python program for student marks and test it using a pytest fixture.

Your task is to create two files: `student.py` and `test_student.py`.

In `student.py`, write a function named `get_average(marks)` that accepts a list of student marks and returns their average.

In `test_student.py`, create a pytest fixture that provides the list `[80, 90, 70]`.

Using that same fixture, write three separate test functions that verify:

1. `get_average(marks)` returns `80`
2. The list contains exactly `3` marks
3. The highest mark in the list is `90`

Do not create `[80, 90, 70]` again inside the test functions. Reuse the fixture in all three tests.

'''

