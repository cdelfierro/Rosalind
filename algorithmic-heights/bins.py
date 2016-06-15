#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock

"""
Binary search
"""
def bins(A, search):
    upper = len(A) - 1
    lower = 0
    while upper >= lower:
        i = (upper + lower) // 2
        if search > A[i]:
            lower = i + 1
        elif search < A[i]:
            upper = i - 1
        else:
            return i + 1
    return -1

try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

n = int(data[0])
m = int(data[1])
A = [int(i) for i in data[2].split()]
search = [int(i) for i in data[3].split()]

start = clock()
finds = [bins(A, i) for i in search]
end = clock()
time = end - start
finds = " ".join(str(i) for i in finds)

with open("output/bins.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(finds + "\n")

print(finds)
print("Time: {} segs.".format(time))
