# 62. Unique Paths
# Medium
# There is a robot on an m x n grid. The robot is initially located at the top-left corner
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that the robot can take
# to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# 2023-06-02 23:23:28
# original
# 2D dp
# time 14.31% space 11.46%
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * n for _ in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]
        return matrix[0][0]


s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 2))
