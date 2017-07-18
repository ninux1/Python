#!/usr/bin/env python

class Parent:
   parentAttr = 100
   def __init__(self):
     print "Calling parent constructor"
   
   def parentMethod(self):
     print "Calling method parent"

   def setAttr(self, attr):
     Parent.parentAttr = attr

   def getAttr(self):
     print "Parent Attr :", Parent.parentAttr

class Child(Parent):
   def childMethod(self):
     print "Calling Child method"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
