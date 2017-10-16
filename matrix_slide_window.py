#!/usr/bin/env python

"""
2x2 window is sliding from top left to bottom right in a 3x3 matrix
nxm = 3x3
k = 2, i.e sliding window size kxk.
"""


class Matrix(object):
    def __init__(self):
        self.matrix = [[1, 5, 3], [3, 2, 11], [4, 1, 9]]
        self.n = 3
        self.m = 3

    def slide(self):
        ri = 0
        k = 2
        while ri < self.n - 1:
            ci = 0
            while ci < self.m - 1:
                print('Sliding to new position')
                for i in range(ri, ri + k):
                    for j in range(ci, ci + k):
                        print(i, j)
                ci += 1
            ri += 1


if __name__ == '__main__':
    m = Matrix()
    m.slide()