#!/usr/bin/env python

s = "silent"
t = "listen"

set1 = repr(s)  # converts string to set

anagram = 1

for i in t:
    if i not in set1:
        anagram = 0
        break

if anagram == 0:
    print("Strings are not anagram")
else:
    print("Strings are anagram")

