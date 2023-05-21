

from typing import List, Optional
from collections import deque, defaultdict


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int,
                           target: int) -> List[List[int]]:
        # construct adj list
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1:])
            graph[edge[1]].append([edge[0], edge[2]])


s = Solution()
print(s.modifiedGraphEdges(5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5))
