#!/usr/bin/env python

"""
This is a sequel from simple_deco1.py file from the same location.
Here we will futher evolve this with actual python decorator syntax.
"""

def called(func):  # This is a function to receive the function to be modified/decorated. i.e decorator This can also be called as wrapper.
    def exe(num):    # This is a new function where the decoration/modification of the original function happens. Also known as decorator.
       return func(num)
    return exe  # Returning the modified function pointer.to the callee

@called
def mul(num):
    print('From the Decorated function {}'.format(num))

foo = called(mul) # foo has the decorated function which is returned from the wrapper function called()
foo(10)
#mul=called(mul)   # Now instead of new function variable what if we replace the original function with its modified/decorated version directly.
#print(mul(10))     # Derefrencing/invoking the decorated/modified function. The Arguments i.e 10 from here directly goes to decorator function exe.