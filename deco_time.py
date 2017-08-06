#!/usr/bin/env python

from datetime import datetime
import time

def timedeco(func):
    def action(num):
        start = datetime.now()
        res = func(num)
        print(res)
        return datetime.now() - start
    return action

@timedeco
def factorial(num):
    result = num
    while(num != 1):
        result = result * (num-1)
        num = num-1
    return result


if __name__ == '__main__':
    print("The time required to execute 6 factorial is {} microseconds".format(factorial(6)))