# 2328. Number of Increasing Paths in a Grid
# Hard
# You are given an m x n integer matrix grid, where you can move from a cell to any adjacent
# cell in all 4 directions.
#
# Return the number of strictly increasing paths in the grid such that you can start from any cell
# and end at any cell. Since the answer may be very large, return it modulo 109 + 7.
#
# Two paths are considered different if they do not have exactly the same sequence of visited cells.
from typing import List


# 2023-06-19 15:14:04
# learned
# DFS + memoization
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        memo = [[0] * n for _ in range(m)]

        def dfs(i, j):
            ans = 1
            for di, dj in ds:
                prev_i, prev_j = i + di, j + dj
                if prev_i == -1 or prev_i == m or prev_j == -1 or prev_j == n or \
                        grid[i][j] <= grid[prev_i][prev_j]:
                    continue
                if memo[prev_i][prev_j] != 0:
                    ans += memo[prev_i][prev_j]
                else:
                    ans += dfs(prev_i, prev_j)
                ans %= MOD
            memo[i][j] = ans
            return ans

        return sum(dfs(i, j) for i in range(m) for j in range(n)) % MOD


s = Solution()
print(s.countPaths([[1, 1], [3, 4]]))
print(s.countPaths([[1], [2]]))
