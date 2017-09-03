#/usr/bin/env python


import os


string = 'The quick brown fox jumped over the lazy dog'

l = string.split(' ')

index = 0
length = len(l) - 1

while index != length:
    temp = l[index]
    l[index] = l[length]
    l[length] = temp
    index += 1
    length -= 1

print("The String reverse is {} ".format(l))




