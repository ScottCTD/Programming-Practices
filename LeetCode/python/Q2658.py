# 2658. Maximum Number of Fish in a Grid
# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
#
# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations
# any number of times:
#
# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally,
# or 0 if no water cell exists.
#
# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or
# (r - 1, c) if it exists.

from typing import List

# 2023-05-13 00:53:02
# contest question
# original
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ds = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(i, j, visited: set) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            r = grid[i][j]
            visited.add((i, j))
            for d in ds:
                coord = (i + d[0], j + d[1])
                if coord in visited:
                    continue
                r += dfs(coord[0], coord[1], visited)
            # visited.remove((i, j))
            return r

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    res = max(res, dfs(i, j, set()))
        return res


s = Solution()
print(s.findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
print(s.findMaxFish([[8, 6], [2, 6]]))
