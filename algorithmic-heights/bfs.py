#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock


def bfs(graph, n_nodes, start=1):
    """Breadth-First Search"""
    dist = {__: -1 for __ in range(1, n_nodes + 1)}
    dist[start] = 0
    Q = [start]

    while Q:
        u = Q.pop(0)
        for v in graph[u]:
            if dist[v] == -1:
                Q.append(v)
                dist[v] = dist[u] + 1

    return [dist[v] for v in range(1, n_nodes + 1)]

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

start = clock()
D = bfs(graph, nodes)
end = clock()
time = end - start
D = " ".join(str(__) for __ in D)

with open("output/bfs.txt", "w", encoding="utf-8", newline="\n") as out_file:
    out_file.write(D + "\n")

print(D)
print("Time: {} segs.".format(time))
