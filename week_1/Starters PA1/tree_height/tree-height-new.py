# python3

import sys, threading
sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, index):
        self.index = index
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def height(self):
        if len(self.nodes) == 0:
            return 1

        return max([(x.height() + 1) for x in self.nodes])

    def __repr__(self):
        return "<{} nodes:{}>".format(self.index, self.nodes)

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def height(self, a):
        if len(a) == 0:
            return 1

        return max([(self.height(self.edge_matrix[i]) + 1) for i in a])

    def compute_height(self):
        self.nodes_flat_list = [Node(x) for x in range(self.n)]

        for i in range(self.n):
            if self.parent[i] != -1:
                parent_node = self.nodes_flat_list[self.parent[i]]
                parent_node.add_node(self.nodes_flat_list[i])

        root_index = self.parent.index(min(self.parent))

        return self.nodes_flat_list[root_index].height()

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
