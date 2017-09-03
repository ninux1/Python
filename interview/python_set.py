#!/usr/bin/env python
"""Python set demos"""

string = "abbabcddbabcdeedebc"
set_str = set()

"""
s = set()  # Defining an empty set.
s = {1, 3, 4, 5} # Defining an initialized set.

if 3 in s:   # this can be done for set.
    print("Found the number")

s.add(6) # only single element can be added to a set in a sorted order
s.update([9,10,11])  # You can update a set, this is not a list but multiple elements are updated.

print(s) 
"""

for i in string:
    if i not in set_str:
        set_str.add(i)

print(set_str)


