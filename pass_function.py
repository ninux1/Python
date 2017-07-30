#!/usr/bin/env python

def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def ops(func,x,y):
    return func(x,y)


print(ops(mul,2,2))

