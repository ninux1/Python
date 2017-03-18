#!/usr/bin/python env

import os
import random 

class DiceSim:
	def __init__(self):
			print "\n"
			print "				---------- Welcome to the dice simulator -----------			"
			print "\n"
			print "					  Lets configure the dice 						  			"
			print "\n"
			self.min_val = input("Enter the minimum value for the dice : ")
			self.max_val = input("Enter the maximum value for the dice : ")
			
			print "\nThe Rolling Dice will have %d sides with below numbers" % (self.max_val) 
			for i in range(self.min_val, self.max_val + 1):
				print i, 
			print '\n'

	def dice_roll(self):
		while(1):
			self.roll = raw_input("Ready to roll the dice (y/n) : ")
			if (self.roll == 'y'):
				print "you got %d " % random.randint(1,6)
			else:
				break

if __name__ == "__main__":
	ob = DiceSim()
	ob.dice_roll()
