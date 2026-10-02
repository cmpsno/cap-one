# guided_extra.py - extra BFS/DFS reps (self-serve). Fill TODOs.
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# Rep 1: BFS order from "A".
# def bfs_order(graph, start):
#     # TODO: queue + visited
#     pass

# Rep 2: DFS order from "A" (iterative stack or recursion).
# def dfs_order(graph, start):
#     # TODO
#     pass

# Rep 3: shortest path A -> F in edges using BFS.
# def shortest_path_bfs(graph, start, goal):
#     # TODO: parent map
#     pass

# Rep 4: count connected components.
# def count_components(graph):
#     # TODO: loop all nodes, BFS/DFS mark visited
#     pass
