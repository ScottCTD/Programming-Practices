# 64. Minimum Path Sum
# Medium
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
# which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
from typing import List

# 2023-06-02 23:32:43
# original
# 2d dp
# time 57.55% space 26.44%
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]
        for i in range(m - 2, -1, -1):
            dp[i][-1] = grid[i][-1] + dp[i + 1][-1]
        for i in range(n - 2, -1, -1):
            dp[-1][i] = grid[-1][i] + dp[-1][i + 1]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]