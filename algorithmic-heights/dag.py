#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys


def explore(graph, node, path):
    """Explore"""
    graph[node]["visited"] = True
    path.append(node)

    for neighbor in graph[node]["neighbors"]:
        if graph[neighbor]["visited"]:
            if neighbor in path:
                return -1
        else:
            if explore(graph, neighbor, path) == -1:
                return -1

    return path.pop()


def dag(graph):
    """Testing Acyclicity"""
    path = list()

    for node in sorted(graph.keys()):
        if not graph[node]["visited"]:
            if explore(graph, node, path) == -1:
                return -1

    return 1

try:
    with open(sys.argv[1], "r", encoding="utf-8") as input_file:
        data = input_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
except:
    data = sys.stdin.read().splitlines()

while data:
    test_result = list()
    num_graphs = int(data.pop(0))

    while num_graphs:
        graph_start_line = data.pop(0)
        if graph_start_line == "":
            num_graphs -= 1

        num_nodes, num_edges = [int(__) for __ in data.pop(0).split()]
        graph = dict()

        while num_edges:
            x, y = [int(__) for __ in data.pop(0).split()]

            if x not in graph:
                graph[x] = {"neighbors": [y], "visited": False}
            else:
                graph[x]["neighbors"].append(y)

            if y not in graph:
                graph[y] = {"neighbors": [], "visited": False}

            num_edges -= 1

        for node in graph:
            graph[node]["neighbors"].sort()

        test_result.append(dag(graph))

test_result = " ".join(str(__) for __ in test_result)
print(test_result)

with open("output/dag.txt", "w", encoding="utf-8", newline="\n") as out_file:
    out_file.write(test_result + "\n")
