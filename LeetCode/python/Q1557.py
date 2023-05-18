# 1557. Minimum Number of Vertices to Reach All Nodes
# Medium
# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where
# edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
#
# Find the smallest set of vertices from which all nodes in the graph are reachable.
# It's guaranteed that a unique solution exists.
#
# Notice that you can return the vertices in any order.

from typing import List

# 2023-05-17 23:05:47
# by hints
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # idea: find all nodes with no incoming edges
        nodes = [True] * n
        for edge in edges:
            nodes[edge[1]] = False
        return [i for i in range(n) if nodes[i]]


s = Solution()
print(s.findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
