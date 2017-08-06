#!/usr/bin/env python

def function(*args):
   for arg in args:
      print(arg)


def kfunction(*args):
   for arg in args:
      print(arg)

#def kwarg(x=1, y=2):
def kwarg(*args, **kwargs):
   #print x ,y 
   for arg in args:
       print(arg)
   for item in kwargs.items():
       print(item)

l = [1,2,3,4,5]
m = [6,7,8,9,10]

#function(1,2,3,4,5,'hans','new')
#function(*l)
#kfunction(*m)
#kwarg()
kwarg(1,2,3,4,5,6,x=7, y=8)
#kfunction(1,2,3,4,5,6,x=7, y=8)
