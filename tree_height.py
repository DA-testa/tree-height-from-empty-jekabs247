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
    input_type = input()

    if input_type.upper() == "I":
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    elif input_type.upper() == "F":
        filename = input()
        if 'a' in filename:
            print()
            return
        try:
            with open("folder/" + filename, 'r') as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
                print(compute_height(n, parents))
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Invalid input type.")


sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()

