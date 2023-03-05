# 221RDC047, Jēkabs Kindzulis, 18.gr.

import numpy as np
import threading


class Node:
    def __init__(self):
        self.children = []


def compute_height(num, parents):
    nodes = [Node() for _ in range(num)]
    root_index = 0

    for child_index in range(num):
        parent_index = parents[child_index]

        if parent_index != -1:
            nodes[parent_index].children.append(nodes[child_index])
        else:
            root_index = child_index

    heights = np.zeros(num, dtype=np.int64)

    def get_height(node):
        if not node.children:
            return 1
        elif heights[node.children[0]] != 0:
            return 1 + heights[node.children[0]]
        else:
            height = 1 + max([get_height(child) for child in node.children])
            heights[node.children[0]] = height - 1
            return height

    return get_height(nodes[root_index])


def main():
    input_str = input()

    if "a" in input_str:
        print()
        return

    if "I" in input_str:
        num = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(num, parents))

    if "F" in input_str:
        filename = input()
        if "a" in filename:
            return
        path = "test/" + filename
        with open(path, 'r') as file:
            num = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            print(compute_height(num, parents))


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()