# 547. Number of Provinces
# Medium
# There are n cities. Some of them are connected, while some are not. If city a is connected
# directly with city b, and city b is connected directly with city c, then city a is connected
# indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside
# of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the
# jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.
from typing import List


class DisjointSet:
    n: int
    parents: List[int]
    rank: List[int]

    def __init__(self, n: int):
        """
        Initializes an int disjoint Set data structure (path compression + union by rank)
        of size n.
        :param n: size
        """
        self.n = n
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        """
        Finds with path compression.
        :param x: x < n
        :return: the representative of the tree that x belongs to
        """
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x: int, y: int) -> None:
        """
        Unions by rank.
        :param x: node x
        :param y: node y
        """
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            self.parents[py] = px
        else:
            self.parents[px] = py
            if self.rank[px] == self.rank[py]:
                self.rank[py] += 1

    def is_connected(self, nodes: List[int]):
        """
        Checks if given nodes are connected.
        :param nodes: given list of nodes
                      Precondition: len(nodes) > 0
        :return: True if connected, or False otherwise
        """
        p = self.find(nodes[0])
        return all(self.find(nodes[i]) == p for i in range(1, len(nodes)))


# 2023-06-03 23:45:59
# original
# union find
# time O(n^2) space O(n)
# for this question, DFS and BFS outperform UF
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ds = DisjointSet(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    ds.union(i, j)
        return len(set(ds.find(i) for i in range(n)))


s = Solution()
print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
