#!/usr/bin/env python

class foo:
    count = 0
    def __init__(self):
        self.__class__.count += 1

if __name__ == "__main__":
    f = foo()
    print(f.count)	
    print(f.__class__.count)
    g = foo()
    print(g.count)
    print(g.__class__.count == g.count)
  
    g.count = 5
    print(g.count)
    print(g.__class__.count)
    print(g.count == g.__class__.count)	
   
    print(f.count)
   
    

