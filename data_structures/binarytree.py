#!/usr/bin/env python


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertnode(data, self.root)

    def insertnode(self, data, node):

        if data < node.data:
            if node.left:
                self.insertnode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if data > node.data:
                if node.right:
                    self.insertnode(data, node.right)
                else:
                    node.right = Node(data)

    def getminvalue(self, node):
        if node.left:
            ret = self.getminvalue(node.left)
            return ret
        else:
            return node.data

    def getmaxvalue(self, node):
        if node.right:
            ret = self.getmaxvalue(node.right)
            return ret
        else:
            return node.data

    def searchvalue(self, node, data):
        if data == node.data:
            return "Match Found"

        if data < node.data:
            if node.left:
                ret = self.searchvalue(node.left, data)
                return ret
            else:
                return "Data not found in left sub tree"
        elif data > node.data:
            if node.right:
                ret = self.searchvalue(node.right, data)
                return ret
            else:
                return "Data not found in right sub tree"
        else:
            return "Data cannot be equal to data in BST"


if __name__ == '__main__':
    tree = BST()
    tree.insert(40)
    tree.insert(25)
    tree.insert(50)
    tree.insert(20)
    tree.insert(10)
    tree.insert(22)
    tree.insert(30)
    tree.insert(38)
    tree.insert(35)
    tree.insert(65)
    tree.insert(60)

    print(tree.searchvalue(tree.root, 22))
    print(tree.searchvalue(tree.root, 21))

    print(tree.getminvalue(tree.root))
    print(tree.getmaxvalue(tree.root))





















