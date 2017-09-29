#!/usr/bin/env python


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        popped = self.stack[-1]
        del self.stack[-1]
        return popped

    def peek(self):
        print("Remaining Elements are {} ".format(self.stack[:]))

if __name__ == '__main__':
    stck = Stack()
    stck.push(10)
    stck.push(20)
    stck.push(30)
    stck.push(40)
    print("popped = {}".format(stck.pop()))
    print("popped = {}".format(stck.pop()))
    stck.peek()

