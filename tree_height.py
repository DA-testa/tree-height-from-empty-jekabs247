# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading

class Node:

    def __init__(self):
        self.children = []

def compute_height(num, parents):

    nodes = [Node() for _ in range(num)]
    root_index = 0

    # Assign children to parents
    for child_index in range(num):
        parent_index = parents[child_index]

        if parent_index != -1:
            nodes[parent_index].children.append(nodes[child_index])
        else:
            root_index = child_index

    def get_height(node):
        if not node.children:
            return 1
        else:
            return 1 + max([get_height(child) for child in node.children])
        
    return get_height(nodes[root_index])

def main():

    input_str = input()

    if "I" in input_str:
        num = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(num, parents))

    if "a" in input_str:
        print()
        return

    if "F" in input_str:
        filename = input()
        if "a" in filename:
            return
        
        path = "test/" + filename

        with open(path, 'r') as file:
            num = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            print(compute_height(num, parents))

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  
    threading.stack_size(2**27) 
    threading.Thread(target=main).start()