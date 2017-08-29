#!/usr/bin/env python


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_node(lst, nod):
    tmp = lst
    while tmp.next is not None:
        tmp = tmp.next
    tmp.next = nod


def print_list(lst):
    while lst.next is not None:
        print(lst.val)
        lst = lst.next


if __name__ == "__main__":
    linked_list = Node(1)
    for i in range(2, 10):
        node = Node(i + 2)
        add_node(linked_list, node)
    print_list(linked_list)