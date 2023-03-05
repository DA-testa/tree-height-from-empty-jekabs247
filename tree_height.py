# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading
import numpy

def find_root(n, children):
    
    for i in range(n):
        if i not in children:
            return i

def compute_height(node, children, heights):
    
    if node in heights:
        return heights[node]
    
    max_height = 0
    if node in children:
        for child in children[node]:
            height = compute_height(child, children, heights)
            max_height = max(max_height, height)
    
    height = max_height + 1
    heights[node] = height
    return height

def main():
    input_method = input()

    if input_method.lower() == 'i':
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        n = int(input())
        parents = list(map(int, input().split()))

    # Build a dictionary of children for each node
    children = {}
    for i in range(n):
        if parents[i] == -1:
            continue
        if parents[i] not in children:
            children[parents[i]] = []
        children[parents[i]].append(i)

    # Find the root node
    root = find_root(n, children)

    # Create an array to store the heights of each node
    heights = {}

    # Calculate the height of each node
    max_height = 0
    if root in children:
        for child in children[root]:
            height = compute_height(child, children, heights)
            max_height = max(max_height, height)

    print(max_height)

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    threading.Thread(target=main).start()