#!/usr/bin/env python


class Sort:
    def __init__(self, arr):
        self.a = arr
        self.low = 0
        self.high = len(self.a) - 1

    def quicksort(self, low, high):
        if low >= high:
            return

        pivot = self.divide(low, high)
        self.quicksort(self.low, pivot-1)
        self.quicksort(pivot+1, high)

    def divide(self, low, high):
        pivotindex = (low + high) // 2
        self.swap(pivotindex, high)

        i = 0
        for j in range(high):
            if self.a[j] < self.a[high]:
                self.swap(i, j)
                i += 1
        self.swap(i, high)
        return i

    def swap(self, i, j):
        temp = self.a[j]
        self.a[j] = self.a[i]
        self.a[i] = temp


if __name__ == '__main__':
    a = [7, 2, 1, 8, 6, 3, 5]
    s = Sort(a)
    s.quicksort(s.low, s.high)
    print(s.a)