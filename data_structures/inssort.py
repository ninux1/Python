#!/usr/bin/env python


def insertion_sort(a):

    for i in range(len(a)-1):
        j = i+1
        while j > 0 and a[j] < a[j-1]:
            swap(a, j)  # This Operation is the bottle neck in insertion sort
            j -=1
    return a


def swap(a, j):
    temp = a[j]
    a[j] = a[j-1]
    a[j-1] = temp

if __name__ == '__main__':
    a = [55, -2, 34, 10, 0, 2, -5, 12]
    print(insertion_sort(a))

