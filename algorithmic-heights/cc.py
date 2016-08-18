#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock


def explore(graph, visited, start):
    """Explore"""
    visited[start] = True

    for v in graph[start]:
        if not visited[v]:
            explore(graph, visited, v)


def cc(graph, n_nodes):
    """Connected Components"""
    visited = {__: False for __ in range(1, n_nodes + 1)}
    ccnum = 0

    for v in range(1, n_nodes + 1):
        if not visited[v]:
            ccnum += 1
            explore(graph, visited, v)

    return ccnum

try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

nodes, edges = [int(__) for __ in data[0].split()]
graph = {__: [] for __ in range(1, nodes + 1)}

for edge in data[1:]:
    for x, y in [edge.split()]:
        graph[int(x)].append(int(y))
        graph[int(y)].append(int(x))

start = clock()
count = cc(graph, nodes)
end = clock()
time = end - start

with open("output/cc.txt", "w", encoding="utf-8", newline="\n") as out_file:
    out_file.write(str(count) + "\n")

print(count)
print("Time: {} segs.".format(time))
