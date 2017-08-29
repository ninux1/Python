#!/usr/bin/env python

"""Tuples are simply a comma separated list of elements but cannot be modified like list
   and are also know as immutable"""

t = (1,2,3,4)
s = (5,6,7,8)

t = t + s

print(type(t))
print(type(s))

print(t)

t = tuple('lupins')

print(t)













