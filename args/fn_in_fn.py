#!/usr/bin/env python

"""
Its tricky below
from called function below mul(6) invokes directly mul function with parameter 6 which prints 6
but returns nothing, so called() function below gets called with None and nothing happens.
But this is not the way a decorator works.
"""


def called(func):
    def exe(num):
       return func(num)
    return exe


def mul(num):
    print(num)


called(mul(6))  # OR called(None)





