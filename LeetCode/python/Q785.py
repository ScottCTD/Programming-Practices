# 785. Is Graph Bipartite?
# Medium
# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1.
# You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to.
# More formally, for each v in graph[u], there is an undirected edge between node u and node v.
# The graph has the following properties:
#
# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is
# no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that
# every edge in the graph connects a node in set A and a node in set B.
#
# Return true if and only if it is bipartite.
from typing import List
from collections import deque

# 2023-05-18 23:45:57
# original
# DFS
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
            n = len(graph)
            s1 = [False] * n
            s2 = [False] * n

            def dfs(node: int, is_s1: bool):
                if is_s1:
                    s1[node] = True
                else:
                    s2[node] = True
                for child in graph[node]:
                    if is_s1:
                        if s1[child]:
                            return False
                        if s2[child]:
                            continue
                    else:
                        if s2[child]:
                            return False
                        if s1[child]:
                            continue
                    if not dfs(child, not is_s1):
                        return False
                return True

            for i in range(n):
                if s1[i] or s2[i]:
                    continue
                if not dfs(i, True):
                    return False
            return True


# 2023-05-18 23:46:10
# BFS
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        s = [0] * n
        for i in range(n):
            if s[i] != 0:
                continue
            q = deque([i])
            s[i] = 1
            while q:
                node = q.popleft()
                for child in graph[node]:
                    if s[child] != 0:
                        if s[child] == s[node]:
                            return False
                    else:
                        s[child] = -s[node]
                        q.append(child)
        return True




s = Solution2()
print(s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False)
print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True)
print(s.isBipartite([[1], [0], [3], [2]]) is True)
print(s.isBipartite([[1], [2], [0]]) is False)
print(s.isBipartite(
    [[3, 4, 6], [3, 6], [3, 6], [0, 1, 2, 5], [0, 7, 8], [3], [0, 1, 2, 7], [4, 6], [4], []]) is True)
