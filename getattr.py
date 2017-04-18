#!/usr/bin/env python

class Employee:
   def __init__(self):
     self.name = "xyz"
     self.sal = 3400
     self.desig = "Consultant"

emp = Employee()

for key in ["name","sal","desig"]:
   print(getattr(emp, key, None))	
	
