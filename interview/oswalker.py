#!/usr/bin/env python

import os


def oswalker(path):
    for (root, sdir, files) in os.walk(path, topdown=False):
        for file in files:
            print(os.path.join(root, file))


if __name__ == '__main__':
    oswalker('C:\Pycharm\Python')
