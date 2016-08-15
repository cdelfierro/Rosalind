#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock


def mer(A, B):
    """Merge two sorted arrays"""
    result = list()
    while len(A) and len(B):
        if A[0] < B[0]:
            result.append(A.pop(0))
        else:
            result.append(B.pop(0))
    return result + A + B


try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

n = int(data[0])
m = int(data[2])
A = [int(__) for __ in data[1].split()]
B = [int(__) for __ in data[3].split()]

start = clock()
merge = mer(A, B)
end = clock()
time = end - start
merge = " ".join(str(__) for __ in merge)

with open("output/mer.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(merge + "\n")

print(merge)
print("Time: {} segs.".format(time))
