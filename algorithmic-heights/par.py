#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock


def par(A):
    """2-Way Partition"""
    result = list()
    test = A.pop(0)
    result.append(test)
    for value in A:
        if test <= value:
            result.append(value)
        else:
            result.insert(0, value)
    return result


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
result = par(A)
end = clock()
time = end - start
result = " ".join(str(__) for __ in result)

with open("output/par.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(result + "\n")

print(result)
print("Time: {} segs.".format(time))
