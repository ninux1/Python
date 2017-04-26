#!/usr/bin/env python

import os


class sample():
   def __init__(self):
	self.age = 35
	self.sport = 'Table Tennis'
	self.paddle = 'viscaria'
	self.blade = 'ml5'
	self.a = 5
	self.b = 6 

   def addition(self):
	print self.a+self.b


if __name__ == "__main__":
   s = sample()
   s.addition()
