#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys
from time import clock

"""
Double-Degree array
"""
def ddeg(graph):
    n_nodes, n_edges = graph[0]
    adj_list = [[] for i in range(n_nodes)]
    ddegree = [0] * n_nodes

    for edge in graph[1:]:
        adj_list[edge[0] - 1].append(edge[1])
        adj_list[edge[1] - 1].append(edge[0])

    for node, nodes_list in enumerate(adj_list):
        for adj_node in nodes_list:
            ddegree[node] += len(adj_list[adj_node - 1])

    return ddegree

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
double_degree = " ".join(str(i) for i in ddeg(graph))
end = clock()
time = end - start

with open("output/ddeg.txt", "w", encoding="utf-8", newline="\n") as out_file:
    out_file.write(double_degree + "\n")

print(double_degree)
print("Time: {} segs.".format(time))
