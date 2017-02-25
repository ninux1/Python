#!/usr/bin/env python

import os

filename = raw_input("Enter filename :")

fd = open(filename, 'w')

line1 = raw_input("Enter the first line :")
line2 = raw_input("Enter the second line :")
line3 = raw_input("Enter the third line :")

fd.write(line1)
fd.write("\n")
fd.write(line2)
fd.write("\n")
fd.write(line3)

fd.close()
