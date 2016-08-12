#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock


def maj(A):
    """Majority element"""
    candidate, count = -1, 0

    for element in A:
        if count == 0:
            candidate, count = element, 1
        elif element != candidate:
            count -= 1
        elif element == candidate:
            count += 1

    if A.count(candidate) > len(A) // 2:
        return candidate

    return -1


try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

k, n = [int(i) for i in data[0].split()]
lists = [[int(i) for i in A.split()] for A in data[1:]]

start = clock()
elements = [maj(A) for A in lists]
end = clock()
time = end - start
elements = " ".join(str(i) for i in elements)

with open("output/maj.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(elements + "\n")

print(elements)
print("Time: {} segs.".format(time))
