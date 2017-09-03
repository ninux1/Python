#/usr/bin/env python


""" Python String reverse without using inbuilt function
Actually we can string reverse with single line
convert string to list and then do list[::-1] which means
start from last element and go back step which reverses the string """


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


