# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading
import numpy

def find_root(n, parents):
    # Find the root node
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
            break
    return root

def compute_height(n, parents):
    # Find the root node
    root = find_root(n, parents)

    # Create an array to store the heights of each node
    heights = numpy.zeros(n, dtype=numpy.int64)

    # Calculate the height of each node
    max_height = 0
    for i in range(n):
        if heights[i] != 0:
            continue
        height = 0
        node = i
        while node != -1:
            if heights[node] != 0:
                height += heights[node]
                break
            height += 1
            node = parents[node]
        heights[i] = height
        max_height = max(max_height, height)

    return max_height

def main():
    input_method = input()

    if input_method.lower() == 'i':
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parent of each node: ").split()))
    else:
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parent of each node: ").split()))
        
    sys.setrecursionlimit(10**9)
    threading.stack_size(2**32)
    threading.Thread(target=print, args=(compute_height(n, parents),)).start()

if __name__ == '__main__':
    main()