#!/usr/bin/env python

"""
Plz refer to simple_deco.py for some reference on decorators.
This syntax may not be exactly like the decorator but its the same
for exact syntax plz refer to actual_deco.py at same location.
"""

def called(func):  # This is a function to receive the function to be modified/decorated. i.e decorator
    def exe(num):    # This is a new function where the decoration/modification of the original function happens.
       return func(num)
    return exe  # Returning the modified function pointer.to the callee

def mul(num):
    print('From the Decorated function {}'.format(num))

#foo = called(mul)   # foo has the decorated function which is returned from the wrapper function called()
mul=called(mul)    # Now instead of new function variable what if we replace the original function with its modified/decorated version directly.
print(mul(10))    # Derefrencing to execute/invoke the decorated function.