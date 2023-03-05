# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading

class Node:

    def __init__(self):
        self.children = []

def tree_height(num_nodes, parents):

    nodes = [Node() for _ in range(num_nodes)]
    root = 0

    for child in range(num_nodes):
        parent = parents[child]

        if parent != -1:
            nodes[parent].children.append(nodes[child])
        else:
            root = child

    def height(node):
        if not node.children:
            return 1
        else:
            return 1 + max([height(child) for child in node.children])
        
    return height(nodes[root])

def main():

    str = input()

    if "I" in str:
        num_nodes = int(input())
        parents = list(map(int, input().split()))
        print(tree_height(num_nodes, parents))

    if "a" in str:
        print()
        return

    if "F" in str:
        fname = input()
        if "a" in fname:
            return
        
        p = "test/" + fname

        with open(p, 'r') as file:
            num_nodes = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            print(tree_height(num_nodes, parents))

if __name__ == "__main__":
    
    sys.setrecursionlimit(10**7)  
    threading.stack_size(2**27) 
    threading.Thread(target=main).start()