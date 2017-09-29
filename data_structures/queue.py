#!/usr/bin/env python

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dqueue(self):
        del self.queue[0]

    def peek(self):
        for i in self.queue:
            print("The Remaining elements in the queue are {}".format(i))

if __name__ == '__main__':
    queue = Queue()
    if queue.isEmpty():
        for i in range(10):
            queue.enqueue(i)

    queue.dqueue()
    queue.dqueue()
    queue.dqueue()

    queue.peek()


