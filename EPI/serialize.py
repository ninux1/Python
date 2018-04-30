#!/usr/bin/env python


import json

'''
This demostrates the Json encoding and decoding capability of python.
json.loads
json.load
json.dump
json.dumps
'''

'''
j = json.load(open("test.json"))
print(j['total'])
'''

with open("test.json", "r") as fp:
    data = fp.read()
    j = json.loads(data)
    for key, value in j.items():
        print(value)