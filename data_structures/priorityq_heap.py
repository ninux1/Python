#!/usr/bin/env python

import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.idx = 0

    def add_item(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.idx, item))
        self.idx += 1

    def next_item(self):
        return heapq.heappop(self.queue)[-1]


if __name__ == '__main__':

    item_q = PriorityQueue()

    while True:
        try:
            inp = input()
            inp = inp.strip()
            lst = list(inp.split(' '))
            if lst[0] in 'ENQUEUE':
                item_q.add_item(lst[1], int(lst[2]))
            elif lst[0] in 'DEQUEUE':
                print(item_q.next_item())
            else:
                exit(0)
        except EOFError:
            break