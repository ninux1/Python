#!/usr/bin/env python


a = [20, 30, 15, 7, 1, -3, -4, 6, 100, -1, 21, 200, 0, 16]


for i in range(len(a) - 1):
    index = i
    for j in range(i+1, len(a)):
        if a[j] < a[index]:
            index = j

    if index is not i:
        temp = a[index]
        a[index] = a[i]
        a[i] = temp

print("The sorted is {} ". format(a))



