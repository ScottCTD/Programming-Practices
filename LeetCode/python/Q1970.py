# 1970. Last Day Where You Can Still Cross
# There is a 1-based binary matrix where 0 represents land and 1 represents water.
# You are given integers row and col representing the number of rows and columns in the matrix,
# respectively.
#
# Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with
# water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the
# ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with
# water (i.e., changed to 1).
#
# You want to find the last day that it is possible to walk from the top to the bottom by only
# walking on land cells. You can start from any cell in the top row and end at any cell in the
# bottom row. You can only travel in the four cardinal directions (left, right, up, and down).
#
# Return the last day where it is possible to walk from the top to the bottom by only walking on
# land cells.
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


# 2023-06-30 00:29:06
# partially original
# disjoint set on water cells
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # every cell and 1 for left, 1 for right (two additonal representatives)
        ds = DisjointSet(row * col + 2)
        D = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        grid = [[0] * col for _ in range(row)]
        for i in range(row * col):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 1
            i1 = r * col + c + 1
            for dr, dc in D:
                new_r, new_c = r + dr, c + dc
                if new_r == -1 or new_c == -1 or new_r == row or new_c == col or \
                        grid[new_r][new_c] == 0:
                    continue
                i2 = new_r * col + new_c + 1
                ds.union(i1, i2)
            # water on the leftmost
            if c == 0:
                ds.union(0, i1)
            elif c == col - 1:
                ds.union(row * col + 1, i1)
            if ds.find(0) == ds.find(row * col + 1):
                return i
        return row * col + 1


s = Solution()
print(s.latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]))  # 1
print(s.latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]))  # 2
print(s.latestDayToCross(3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2],
                                [3, 1]]))  # 3
