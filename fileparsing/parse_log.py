#!/usr/bin/env python

import json


"""
Code to parse the log file and out should be in the below format.
{
    'Date': '2015-05-22 16:46:46,985',
    'Type': 'INFO',
    'Message':'Starting to Wait for Files'
}
...

{
    'Date': '2015-05-22 16:48:48,180',
    'Type': 'ERROR',
    'Message':'Failed: Waiting for files the Files from Cloud Storage:  gs://folder/anotherfolder/ Traceback (most recent call last):
               File "<ipython-input-16-132cda1c011d>", line 10, in <module> if numFilesDownloaded == 0: NameError: name 'numFilesDownloaded' is not defined '
}
"""


def parse_log(logfile):
    mydict = {}
    num = 0
    with open(logfile, 'r') as fp:
        for line in fp:
            if line.startswith('2015'):
                temp = line.split(' - ')
                tempdict = {'Date':temp[0], 'Type':temp[2], 'Message':temp[3]}
                mydict[num] = tempdict

        with open('out.json', 'w') as wp:
            json.dump(mydict, wp)

if __name__ == '__main__':
    parse_log("apache.log")