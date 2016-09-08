#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock


def merge(A, B):
    """Merge two sorted arrays"""
    result = list()
    while len(A) and len(B):
        if A[0] < B[0]:
            result.append(A.pop(0))
        else:
            result.append(B.pop(0))
    return result + A + B


def ms(A):
    """Merge sort"""
    queue = [[__] for __ in A]
    while(len(queue) > 1):
        first = queue.pop(0)
        second = queue.pop(0)
        merged = merge(first, second)
        queue.append(merged)
    return queue[0]


try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

n = int(data[0])
A = [int(__) for __ in data[1].split()]

start = clock()
result = ms(A)
end = clock()
time = end - start
result = " ".join(str(__) for __ in result)

with open("output/ms.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(result + "\n")

print(result)
print("Time: {} segs.".format(time))
