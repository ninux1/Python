#!/usr/bin/env python


class Common(object):
    def __init__(self):
        self.A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30]
        self.B = [6, 7, 20, 21, 30, 85]

    def intersection(self):
        mi = 0
        alen = len(self.A)
        blen = len(self.B)

        for i in range(min(alen, blen)):
            for j in range(mi, max(alen, blen)):
                if self.B[i] == self.A[j]:
                    print(self.B[i])
                    mi = j


if __name__ == '__main__':
    ob = Common()
    ob.intersection()