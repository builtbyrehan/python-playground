''' we are going to solve a problem in which we are asked to define a parametrized pytest function
in order to check possible cases for an even number to be true and non-even to be false

i.e. 
1 -> false
2-> True
6-> True

'''

def is_even(num):
    if num % 2 == 0:
        return True
    return False
