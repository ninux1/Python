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
    nl = Node('L')
    nm = Node('M')
    nn = Node('N')
    no = Node('O')
    np = Node('P')
    nr = Node('R')
    ns = Node('S')
    nt = Node('T')
    nu = Node('U')
    nx = Node('X')
    nw = Node('W')
    ny = Node('Y')
    nz = Node('Z')


    # define edges/connections.

    na.neighbors.append(nb)
    na.neighbors.append(nc)
    na.neighbors.append(ne)

    nc.neighbors.append(nf)
    nc.neighbors.append(ng)
    nc.neighbors.append(nd)

    nf.neighbors.append(nh)
    nh.neighbors.append(nz)

    ng.neighbors.append(ni)
    ni.neighbors.append(ny)

    nb.neighbors.append(nl)
    nl.neighbors.append(nm)
    nm.neighbors.append(nn)

    nn.neighbors.append(no)
    nn.neighbors.append(np)

    ne.neighbors.append(nu)
    ne.neighbors.append(nx)
    ne.neighbors.append(nw)
    ne.neighbors.append(nt)

    nt.neighbors.append(nr)
    nt.neighbors.append(ns)

    dfs = Dfs()
    dfs.pushq_iterate(na)