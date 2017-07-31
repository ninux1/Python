#!/usr/bin/env python

def function(*args):
   for arg in args:
      print arg


def kfunction(*args):
   for arg in args:
      print arg

def kwarg(x=1, y=2):
   print x ,y 
   

l = [1,2,3,4,5]
m = [6,7,8,9,10]

#function(1,2,3,4,5,'hans','new')
#function(*l)
#kfunction(*m)
kwarg()
#kwarg(x=12, y=14)
