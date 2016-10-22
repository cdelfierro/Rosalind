#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Carlos Gómez del Fierro
"""
import sys


def bip(graph):
    """Testing Bipartiteness"""
    start = min(graph)
    queue = [start]
    current_color = 0
    graph[start]["color"] = current_color
    graph[start]["visited"] = True

    while queue:
        current_node = queue.pop(0)

        if graph[current_node]["color"] == 0:
            current_color = 1
        else:
            current_color = 0

        for neighbor in graph[current_node]["neighbors"]:
            if graph[neighbor]["visited"]:
                if graph[neighbor]["color"] == graph[current_node]["color"]:
                    return -1
            else:
                graph[neighbor]["color"] = current_color
                graph[neighbor]["visited"] = True
                queue.append(neighbor)

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
                graph[x] = {"neighbors": [y], "color": None, "visited": False}
            else:
                graph[x]["neighbors"].append(y)

            if y not in graph:
                graph[y] = {"neighbors": [x], "color": None, "visited": False}
            else:
                graph[y]["neighbors"].append(x)

            num_edges -= 1

        for node in graph:
            graph[node]["neighbors"].sort()

        test_result.append(bip(graph))

test_result = " ".join(str(__) for __ in test_result)
print(test_result)

with open("output/bip.txt", "w", encoding="utf-8", newline="\n") as out_file:
    out_file.write(test_result + "\n")
