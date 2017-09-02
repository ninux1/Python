#!/usr/bin/env python

# A Simple matrix Program demonstrating map functionality

matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Addition of the list elements Can be done as below for loop.

#for index in matrix:
#	print(sum(index))

# Is same as below 
# Map function always returns a list
# So the below statement expands to "sum of each element in the matrix list"
# Also the sum function below needs a iterable entity like list
# So the whole for construct can be done using a single map function

print(list(map(sum, matrix)))

