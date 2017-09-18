#!/usr/bin/env python

import requests
import json


url = 'http://127.0.0.1:5000/messages'


#r = requests.get(url + '/articles')

#print(r.status_code)
#print(r.headers)
#print(r.text)
#print(r.url)
#print(r.encoding)


payload = { 'name': 'Ninad', 'job': 'software_engineering' }
headers = {'Content-Type' : 'application/json, charset=utf-8'}

resp = requests.post(url, data=json.dumps(payload), headers= headers)

print(resp.status_code)
#print(resp.text)
print(json.dumps(resp.json()))








