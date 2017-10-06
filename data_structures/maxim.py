#!/usr/bin/env python


class Seq:
    def __init__(self, array):
        self.array = array

    def findmissing(self):
        for i in range(len(self.array)):
            if i not in self.array:
                return i


if __name__ == '__main__':
    raw = input()
    array = list(map(int, raw.split(' ')))
    l = Seq(array)
    print("The missing number is {}".format(l.findmissing()))