#!/usr/bin/env python

""" This python program takes in the path and prints all the contents from subdirectories as well"""

import os

def listdir(path):
   if(os.path.isdir(path)):
        for file in os.listdir(path):
            filepath = os.path.join(path, file)
            if os.path.isdir(filepath):
                listdir(filepath)
            else:
                print(filepath)
   else:
       print("Plz enter a path to a directory")

listdir('C:\Pycharm\Python')


