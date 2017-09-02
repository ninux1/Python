#!/usr/bin/env python

import glob

""" glob.glob gives us all the contents of the particular directory and does 
    not recurse in the sub directories."""

for name in glob.glob('C:\Pycharm\Python\*'):
    print(name)
