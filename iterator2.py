#!/usr/bin/env python


class Array:
    def __init__(self, data):
        self.array = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.array):
            raise StopIteration
        return self.array[self.index]

if __name__ == '__main__':
    a1 = [1,2,3,4,7,9]
    a2 = [3,5,6,8,10]

    A2 = Array(a2)
    for i in A2:
        a1.append(i)
    a1.sort()
    print(a1)


