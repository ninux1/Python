#!/usr/bin/env python


class Sort:
    def __init__(self, arr):
        self.a = arr
        self.low = 0
        self.high = len(self.a) - 1

    def quicksort(self, low, high):
        if low >= high:
            return

        pivot = self.divide()
        self.quicksort(self.low, pivot-1)
        self.quicksort(pivot+1, self.high)

    def divide(self):
        pivotindex = (self.low + self.high) // 2
        self.swap(pivotindex, self.high)

        i = 0
        for j in range(len(self.a)):
            if self.a[j] < self.a[self.high]:
                self.swap(i, j)
                i += 1
        self.swap(i, self.high)
        print(i)
        return i

    def swap(self, i, j):
        temp = self.a[j]
        self.a[j] = self.a[i]
        self.a[i] = temp


if __name__ == '__main__':
    #inp = input()
    #a = list(map(int, inp.split(' ')))
    a = [7, 2, 1, 8, 6, 3,5]

    s = Sort(a)
    s.quicksort(s.low, s.high)
    print(s.a)