# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading
import numpy


def compute_height(n, parents):

    heights = numpy.zeros(n, dtype=numpy.int64)
    max_height = 0

    for i in range(n):

        current = i
        height = 0

        while current != -1:

            if heights[current] != 0:
                height += heights[current]
                break

            height += 1
            current = parents[current]

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
        
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    threading.Thread(target=print, args=(compute_height(n, parents),)).start()

if __name__ == '__main__':
    main()