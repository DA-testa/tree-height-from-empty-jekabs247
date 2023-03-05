# 221RDC047, Jēkabs Kindzulis, 18.gr.

import sys
import threading

class Node:

    def _init_(self):
        self.children = []

def calculateHeight(num, parents):

    node = [Node() for _ in range(num)]
    rootPlace = 0

    for childPlace in range(num):
        parentPlace = parents[childPlace]

        if parentPlace != -1:
            node[parentPlace].children.append(node[childPlace])
        else:
            rootPlace = childPlace

    return heightVal(node[rootPlace])


def heightVal(node):

    if not node.children:
        return 1
    else:
        return 1 + max([heightVal(child) for child in node.children])


def main():

    imput = input()

    if "a" in imput:
        print()
        return

    if "I" in imput:
        num = int(input())
        parents = list(map(int, input().split()))
        print(calculateHeight(num, parents))

    if "F" in imput:

        file = input()
        if "a" in file:
            return
        path = "test/" + file

        with open(path, 'r') as file:

            num = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            print(calculateHeight(num, parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()