#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock

"""
Degree array
"""
def deg(graph):
    n_nodes, n_edges = graph[0]
    degree = [0] * n_nodes
    for edge in graph[1:]:
        degree[edge[0] - 1] += 1
        degree[edge[1] - 1] += 1
    return degree

try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

graph = [(int(x), int(y)) for edge in data for x, y in [edge.split()]]

start = clock()
degree = " ".join(str(i) for i in deg(graph))
end = clock()
time = end - start

with open("output/deg.txt", "w", encoding="utf-8", newline="\n") as out_file:
    out_file.write(degree + "\n")

print(degree)
print("Time: {} segs.".format(time))
