#!/usr/bin/env python

import os


def listfiles(path):
    for i in os.listdir(path):
        if os.path.isdir(i):
            listfiles(i)
        else:
            print(os.path.join(os.path.abspath(path), i))


listfiles(".")