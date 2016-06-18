#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock

"""
Insertion sort
"""
def ins(A):
    swaps = 0
    for i in range(1, len(A)):
        target = i
        while target >= 1 and A[target] < A[target - 1]:
            A[target - 1], A[target] = A[target], A[target - 1]
            swaps += 1
            target -= 1
    return swaps

try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

A = [int(x) for x in data[1].split()]

start = clock()
swaps = ins(A)
end = clock()
time = end - start

with open("output/ins.txt", "w", encoding="utf-8", newline="\n") as out_file:
    out_file.write(str(swaps) + "\n")

print(swaps)
print("Time: {} segs.".format(time))
