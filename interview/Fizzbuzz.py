#!/usr/bin/env python

#Print a list of n fizzbuzz numbers


def fizzbuzz(n):
    fizzbuzzl = []
    num = 1
    while len(fizzbuzzl) <= n:
        if num % 3 == 0 or num % 5 == 0:
            fizzbuzzl.append(num)
        num += 1
    print("First 30 fizz numbers are {}".format(fizzbuzzl))

if __name__ == '__main__':
    fizzbuzz(30)