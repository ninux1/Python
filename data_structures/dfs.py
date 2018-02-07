#!/usr/bin/env python


class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = 0
        self.neighbors = []


class Dfs(object):
    def __init__(self):
        self.S = []

    def pushq_iterate(self, node):
        node.visited = 1
        self.S.append(node)
        print("Inserted node {}".format(node.name))
        if node.neighbors:
            for n in node.neighbors:
                if n.visited is 0:
                    self.pushq_iterate(n)
            p = self.S.pop()
            print("Popped parent node {}".format(p.name))
        else:
            p = self.S.pop()
            print("No neighbors popped node {}".format(p.name))


if __name__ == "__main__":

    # Initialize the nodes

    na = Node('A')
    nb = Node('B')
    nc = Node('C')
    nd = Node('D')
    ne = Node('E')
    nf = Node('F')
    ng = Node('G')
    nh = Node('H')
    ni = Node('I')

    # define edges/connections.

    na.neighbors.append(nb)
    na.neighbors.append(nc)

    nb.neighbors.append(nd)
    nb.neighbors.append(ne)
    ne.neighbors.append(nh)

    nc.neighbors.append(nf)
    nc.neighbors.append(ng)
    nf.neighbors.append(ni)

    dfs = Dfs()
    dfs.pushq_iterate(na)
