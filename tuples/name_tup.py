
#!/usr/bin/env python

from collections import namedtuple

""" Demonstrating named tuple, named tuple helps you take field names instead of indexes becoz  
    if elements grows addressing elements with indexes become difficult, so field names come to rescue """

named = namedtuple('named','name, add')

p1 = named(10, 20)
p2 = named(30, 40)

print(p1.name)
print(p2.name)

print(named._fields)


