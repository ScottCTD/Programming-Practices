# 399. Evaluate Division
# Medium
# Companies
# You are given an array of variable pairs equations and an array of real numbers values,
# where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
# Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where
# you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries will not result in
# division by zero and that there is no contradiction.
from collections import deque, defaultdict
from typing import List


# 2023-05-20 14:59:49
# original implementation but inspired idea
# BFS
# we may augment it by memoization, or change to DFS might be better
# not so efficient
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (v1, v2) in enumerate(equations):
            graph[v2].append((v1, values[i]))
            graph[v1].append((v2, 1 / values[i]))
        r = []
        for (v1, v2) in queries:
            if v2 not in graph:
                r.append(-1.0)
                continue
            visited = set()
            q = deque()
            success = False
            q.append((v2, 1.0))
            while q:
                node = q.popleft()
                visited.add(node[0])
                if node[0] == v1:
                    r.append(node[1])
                    success = True
                    break
                for child in graph[node[0]]:
                    if child[0] in visited:
                        continue
                    q.append((child[0], node[1] * child[1]))
            if not success:
                r.append(-1.0)
        return r


s = Solution()
print(s.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                     [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.00000,
                                                                                       0.50000,
                                                                                       -1.00000,
                                                                                       1.00000,
                                                                                       -1.00000])
print(s.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
                     [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]) == [3.75000, 0.40000,
                                                                               5.00000, 0.20000]
      )
print(s.calcEquation([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]) == [
    0.50000, 2.00000, -1.00000, -1.00000])
print(s.calcEquation([["a", "b"], ["b", "c"], ["a", "c"]], [2.0, 3.0, 6.0],
                     [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.0, 0.5,
                                                                                       -1.0, 1.0,
                                                                                       -1.0])
