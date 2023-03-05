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
    
    if choice == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        file_name = input()
        with open(file_name, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))

    print(compute_height(n, parents))

# Set the recursion depth limit and stack size for the new thread
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()