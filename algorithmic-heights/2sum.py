#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock


def two_sum(A):
    """2sum"""
    indexes = {value: index for index, value in enumerate(A)}

    for index, value in enumerate(A):
        if -value in indexes:
            return str(index + 1) + " " + str(indexes[-value] + 1)

    return -1


try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

k, n = [int(__) for __ in data[0].split()]
lists = [[int(__) for __ in A.split()] for A in data[1:]]

start = clock()
sums = [two_sum(A) for A in lists]
end = clock()
time = end - start
sums = "\n".join(str(__) for __ in sums)

with open("output/2sum.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(sums + "\n")

print(sums)
print("Time: {} segs.".format(time))
