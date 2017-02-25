#!/usr/bin/python env

import os

class Box():
    def __init__(self,length, breadth, height):
        self.len = length
        self.brd = breadth
        self.hgt = height
    def area(self):
        print "The area of box is %d " %(self.len * self.brd)
    def volume(self):
        print "The volume of box is %d " %(self.len*self.brd*self.hgt)

if __name__ == "__main__":

    length = int(raw_input("Enter the length of the Box :"))
    breadth = int(raw_input("Enter the breadth of the Box :"))
    height = int(raw_input("Enter the height of the Box :"))

    vol = Box(length,breadth,height)

    print vol.len
    print vol.brd
    print vol.hgt

    vol.area()
    vol.volume()
