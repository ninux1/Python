#!/usr/bin/env python


a = [20, 30, 15, 7, 1, -3, -4, 6, 100, -1, 21, 200, 0, 16]

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print(" The sorted list is {}".format(a))
