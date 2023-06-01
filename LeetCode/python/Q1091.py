# 1091. Shortest Path in Binary Matrix
# Medium
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
# If there is no clear path, return -1.
#
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the
# bottom-right cell (i.e., (n - 1, n - 1)) such that:
#
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected
# (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

from typing import List


# 2023-06-01 00:11:08
# original
# BFS
# time 50.88% space 12.33%
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        queue = [(0, 0)]
        visited = set()
        depth = 0
        while queue:
            new_queue = []
            for coord in queue:
                if coord in visited:
                    continue
                visited.add(coord)
                i, j = coord
                if i == n - 1 and j == n - 1:
                    return depth + 1
                for di, dj in ds:
                    new_i, new_j = i + di, j + dj
                    if new_i == -1 or new_i == n or new_j == -1 or new_j == n or \
                            grid[new_i][new_j] == 1:
                        continue
                    new_queue.append((new_i, new_j))
            queue = new_queue
            depth += 1
        return -1


s = Solution()
print(s.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
print(s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(s.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
