#!/usr/bin/env python


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(10)

    def addnode(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def remove_node(self, data):
        temp = self.head
        prevnode = None

        while temp is not None:
            if temp.data == data:
                prevnode.next = temp.next
                temp = None
                break
            prevnode = temp
            temp = temp.next


if __name__ == '__main__':
    lst = LinkedList(Node)
    lst.addnode(20)
    lst.addnode(30)
    lst.addnode(40)
    lst.addnode(50)
    lst.print_list()
    lst.remove_node(30)
    lst.print_list()