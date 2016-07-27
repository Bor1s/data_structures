# python3
import sys, threading, os, timeit
sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                # self.n = int(sys.stdin.readline())
                # self.parent = list(map(int, sys.stdin.readline().split()))

                # Read input from test file
                os.chdir('tests')
                f = open('18','r')
                self.n = int(f.readline())
                self.parent = list(map(int, f.readline().split()))
                self.max_depth = 0

        def compute_height_naive(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                start_time = timeit.default_timer()
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                elapsed = timeit.default_timer() - start_time
                print(elapsed)
                return maxHeight;

        def compute_height_fast(self):
            # Replace this code with a faster implementation
            maxHeight = 0
            tree = [None]*self.n
            current_depth = 0

            start_time = timeit.default_timer()

            for index, vertex in enumerate(self.parent):
                if vertex == -1:
                    continue

                if isinstance(tree[vertex],list):
                    tree[vertex].append(index)
                else:
                    tree[vertex] = [index]

            for el in tree:
                  self.foo(el, tree, current_depth)

            elapsed = timeit.default_timer() - start_time
            print(elapsed)

            return self.max_depth + 1

        def foo(self, el, tree, current_depth):
            if isinstance(el, list):
                current_depth += 1
                for i in el:
                    self.foo(tree[i], tree, current_depth)
            else:
                if current_depth > self.max_depth:
                    self.max_depth = current_depth

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height_fast())
  # print(tree.compute_height_naive())

threading.Thread(target=main).start()
