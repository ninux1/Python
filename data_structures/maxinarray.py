#!/usr/bin/env python


num = [10, 20, 300, 40.5, 50, 600]

max = num[0]

for i in num:
    if i > max:
        max = i

print("The Max number is {}".format(max))


