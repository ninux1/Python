#!/usr/bin/env python

"""
But this a way to think about decorators.
Decorator is a function which takes one function and returns the decorated/modified version of that function.
The Next step to this code is in simple_deco1.py in the same location
"""

def called(func):  # This is a function to receive the function to be modified/decorated. i.e decorator
    def exe(num):    # This is a new function
       return func(num)
    return exe

def mul(num):
    print('From the Decorated function {}'.format(num))

foo = called(mul)   # foo has the decorated function which is returned from the wrapper function called()
print(foo(10))    # finally invoking OR derefrencing the foo to call execute the decorated function.




