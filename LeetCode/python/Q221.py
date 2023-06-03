# 221. Maximal Square
# Medium
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's
# and return its area.
from typing import List


# 2023-06-03 00:39:02
# learned
# 2D dp
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        side = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    side = max(side, dp[i][j])
                else:
                    dp[i][j] = 0
        return side ** 2


s = Solution()
print(s.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]))
