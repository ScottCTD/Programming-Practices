# 1514. Path with Maximum Probability
# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list
# where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of
# success of traversing that edge succProb[i].
#
# Given two nodes start and end, find the path with the maximum probability of success to go from
# start to end and return its success probability.
#
# If there is no path from start to end, return 0. Your answer will be accepted if it differs from
# the correct answer by at most 1e-5.
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start: int, end: int) -> float:
        # construct the adjacency list
        graph = [[] for _ in range(n)]
        for (v, u), w in zip(edges, succProb):
            graph[v].append((u, w))
            graph[u].append((v, w))
        # perform GBFS, use a max heap stores path probability
        heap = [(-1, start)]
        visited = set()
        ans = 0.0
        while heap:
            # prob is negative
            prob, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if node == end:
                # ans = max(ans, -prob)
                # we can safely return it because the firstly found is guaranteed to be the maximum
                # since we stored the PATH probability, so only the path with the highest prob
                # is considered
                return -prob
            for child_node, child_prob in graph[node]:
                #                     -    * + = -
                heapq.heappush(heap, (prob * child_prob, child_node))
        return ans


s = Solution()
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))  # 0.25
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))  # 0.3
print(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 1.0, 0.3], 0, 2))  # 0.5
print(s.maxProbability(3, [[0, 1]], [0.5], 0, 2))  # 0.0
