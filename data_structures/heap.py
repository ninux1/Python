#!/usr/bin/env python


class Heap:

    HEAPSIZE = 10

    def __init__(self):
        self.heap = []*Heap.HEAPSIZE
        self.CurrentPos = -1

    def heap_push(self, item):
        if self.isfull():
            print("Heap is full Now")
            exit(0)
        else:
            self.CurrentPos = self.CurrentPos + 1
            self.heap.insert(self.CurrentPos, item)
            self.check_heap_prop_add(self.CurrentPos)

    def check_heap_prop_add(self, cidx):
        pidx = (cidx - 1) // 2
        while pidx >=0 and self.heap[pidx][1] < self.heap[cidx][1]:
            self.swap(pidx, cidx)
            cidx = pidx
            pidx = (pidx - 1) // 2

    def heap_pop(self):
        popped = self.heap[0]
        return popped

    def swap(self, pidx, cidx):
        temp = self.heap[pidx]
        self.heap[pidx] = self.heap[cidx]
        self.heap[cidx] = temp

    def isfull(self):
        if len(self.heap) == Heap.HEAPSIZE:
            return True
        else:
            return False


if __name__ == '__main__':
    h = Heap()
    h.heap_push(("Node4", 1))
    h.heap_push(("Node2", 3))
    h.heap_push(("Node3", 4))
    h.heap_push(("Node1", 5))
    h.heap_push(("Node6", 8))
    h.heap_push(("Node5", 6))
    h.heap_push(("Node10", 16))
    print(h.heap_pop())
    print(h.heap)