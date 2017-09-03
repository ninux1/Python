#!/usr/bin/env python


string = 'abbabcddbabcdeedebc'

m = []

for i in string:
    found = 0
    for j in m:
        if i == j:
            found = 1
            break
    if found == 0:
        m.append(i)

print("After removing duplicates {}".format(m))