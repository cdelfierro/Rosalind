#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock


def sink(heap, node):
    """Sink"""
    while node < len(heap) // 2:
        child = (2 * node + 1, 2 * node + 2)

        # Only one child
        if child[1] >= len(heap):
            if heap[child[0]] > heap[node]:
                heap[node], heap[child[0]] = heap[child[0]], heap[node]
                node = child[0]
            else:
                break
        # Two children
        else:
            if heap[child[0]] >= heap[child[1]]:
                if heap[child[0]] > heap[node]:
                    heap[node], heap[child[0]] = heap[child[0]], heap[node]
                    node = child[0]
                elif heap[child[1]] > heap[node]:
                    heap[node], heap[child[1]] = heap[child[1]], heap[node]
                    node = child[1]
                else:
                    break
            else:
                if heap[child[1]] > heap[node]:
                    heap[node], heap[child[1]] = heap[child[1]], heap[node]
                    node = child[1]
                elif heap[child[0]] > heap[node]:
                    heap[node], heap[child[0]] = heap[child[0]], heap[node]
                    node = child[0]
                else:
                    break


def bubble(heap, node, parent):
    """Bubble"""
    while heap[node] > heap[parent] and node > 0:
        heap[node], heap[parent] = heap[parent], heap[node]
        sink(heap, node)
        node = parent
        parent = (node - 1) // 2


def hea(A):
    """Heap"""
    heap = list(A)
    for node in range(len(heap) - 1, 0, -1):
        parent = (node - 1) // 2
        bubble(heap, node, parent)
    return heap

try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

n = data[0]
A = [int(__) for __ in data[1].split()]

start = clock()
heap = hea(A)
end = clock()
time = end - start
heap = " ".join(str(__) for __ in heap)

with open("output/hea.txt", "w", encoding="utf-8", newline="\n") as out_file:
    out_file.write(heap + "\n")

print(heap)
print("Time: {} segs.".format(time))
