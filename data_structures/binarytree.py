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

    def remove(self, node, data):
        if data == node.data:
            if node.left and node.right:
                ret = self.swapmax(node, node.right)
                return ret

    def swapmax(self, root, node):
        if node.right is None:
            ret = self.swap(root, node)
            return ret
        else:
            self.swapmax(root, node.right)

    def swap(self, root, node):
        temp = root.data
        root.data = node.data
        node.data = temp
        return root

    def inorder(self, node):
        if node.left is not None:
            self.inorder(node.left)
        print(node.data)
        if node.right is not None:
            self.inorder(node.right)

    def preorder(self, node):
        print(node.data)
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)

    def postorder(self, node):
        if node.left is not None:
            self.postorder(node.left)
        if node.right is not None:
            self.postorder(node.right)
        print(node.data)


if __name__ == '__main__':
    tree = BST()
    tree.insert(50)
    tree.insert(43)
    tree.insert(65)
    tree.insert(10)
    tree.insert(26)
    tree.insert(28)
    tree.insert(35)
    tree.insert(25)
    tree.insert(30)
    tree.insert(40)
    tree.insert(52)
    tree.insert(51)
    tree.insert(55)
    tree.insert(72)
    tree.insert(80)

    #print(tree.searchvalue(tree.root, 22))
    #print(tree.searchvalue(tree.root, 30))

    #tree.remove(tree.root, 22)
    #tree.remove(tree.root, 21)

    #print(tree.getminvalue(tree.root))
    #print(tree.getmaxvalue(tree.root))
    #tree.inorder(tree.root)
    #tree.preorder(tree.root)
    tree.postorder(tree.root)















