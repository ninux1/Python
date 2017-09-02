#!/usr/bin/env python

import os


def walker(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path,file)):
                print(os.path.join(path,file))
            else:
                walker(os.path.join(path,file))
    else:
        print("enter proper dir path")

if __name__ == '__main__':
    walker('C:\Pycharm\Python')