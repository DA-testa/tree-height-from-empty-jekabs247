# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading

class Node:
    def __init__(self):
        self.children = []

def tree_height(num_nodes, parents):

    nodes = [Node() for _ in range(num_nodes)]
    root_index = 0

    for child_index in range(num_nodes):
        parent_index = parents[child_index]

        if parent_index != -1:
            nodes[parent_index].children.append(nodes[child_index])
        else:
            root_index = child_index

    def height(node):
        if not node.children:
            return 1
        else:
            return 1 + max([height(child) for child in node.children])
        
    return height(nodes[root_index])

def main():

    input_str = input()

    if "I" in input_str:
        num_nodes = int(input())
        parents = list(map(int, input().split()))
        print(tree_height(num_nodes, parents))

    if "a" in input_str:
        print()
        return

    if "F" in input_str:
        filename = input()
        if "a" in filename:
            return
        
        p = "test/" + filename

        with open(p, 'r') as file:
            num_nodes = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            print(tree_height(num_nodes, parents))

if __name__ == "__main__":
    
    sys.setrecursionlimit(10**7)  
    threading.stack_size(2**27) 
    threading.Thread(target=main).start()