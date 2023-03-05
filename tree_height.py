# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading
import numpy

def find_root(n, parents):
    
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
            break
    return root

def compute_height(n, parents):
    
    root = find_root(n, parents)

    heights = numpy.zeros(n, dtype=numpy.int64)

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
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        n = int(input())
        parents = list(map(int, input().split()))

    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    threading.Thread(target=print, args=(compute_height(n, parents),)).start()

if __name__ == '__main__':
    main()