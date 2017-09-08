#!/usr/bin/python

num = 5

try:
    x = num/0
except ZeroDivisionError:
    print("Division by zero")


