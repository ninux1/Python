#!/usr/bin/env python
def wrapper(item):
    def wrapped():
        return "your gift is {}".format(str(item()))
    return wrapped

@wrapper
def gift():
    return "Toyota 4 runner"

@wrapper
def christmas():
    return "Santa Claus"

if __name__ == '__main__':
    print(gift())
    print(christmas())