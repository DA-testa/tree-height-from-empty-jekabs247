# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading
import numpy


def compute_height(n, parents):
    
    heights = [0] * n

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

    return max(heights)

def main():

    choice = input()
    n = int(input())

    parents = list(map(int, input().split()))

    if choice == "I":
        print(compute_height(n, parents))
    else:
        print(compute_height(n, parents))

    #print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()