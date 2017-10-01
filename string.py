#!/usr/bin/env python

import itertools


a = ['ab', 'ab', 'abc', 'bca']
match = 0
case = 0

for i in range(len(a)-1):
    for p in itertools.permutations(a[i]):
        if str(''.join(p)) in a[i+1]:
            match = 1
            break
    if match is not None:
        case += 1
        match = 0

print("the required cases are {}".format(case))