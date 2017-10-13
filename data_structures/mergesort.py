#!/usr/bin/env python


class MergeSort:
    def __init__(self, data):
        self.array = data
        self.sorted = []

    def mergesort(self, low, high):
        mid = (low + high) // 2
        if low >= high:
            print(self.array[low])
            return
        self.mergesort(low, mid)
        self.mergesort(mid+1, high)
        #self.merge(low, high)

    def merge(self, low, high):
        print(low, high)

    def join(self, low, high):
        while True:
            if i < len(a) and j < len(b):
                if a[i] < b[j]:
                    c.append(a[i])
                    i += 1
                else:
                    c.append(b[j])
                    j += 1
            elif i == len(a) and j < len(b):
                c.append(b[j])
                j += 1
            elif j == len(b) and i < len(a):
                c.append(a[i])
                i += 1
            else:
                if i == len(a) and j == len(b):
                    break


if __name__ == '__main__':
    ms = MergeSort([85, 23, 47, 20, 1, 5, 73])
    ms.mergesort(0, len(ms.array) - 1)