# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading

class Node:
    def __init__(self):
        self.children = []

def tree_height(num_nodes, parents):

    heights = {}

    for node_index in range(num_nodes):
        height = 0
        parent_index = parents[node_index]
        while parent_index != -1:
            if parent_index in heights:
                height += heights[parent_index]
                break
            else:
                height += 1
                parent_index = parents[parent_index]
        heights[node_index] = height

    return max(heights.values())

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