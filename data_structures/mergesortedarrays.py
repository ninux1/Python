#!/usr/bin/env python

# Merging 2 sorted arrays into a new merged sorted array.

# a = [23, 60]
a = [23]
# b = [20, 47, 80, 90]
b = [20]
c = []

i = j = 0

while True:
    if i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    elif i == len(a) and j < len(b):
            c.append(b[j])
            j += 1
    elif j == len(b) and i < len(a):
            c.append(a[i])
            i += 1
    else:
        if i == len(a) and j == len(b):
            break
print(c)