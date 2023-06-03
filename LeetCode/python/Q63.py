# 63. Unique Paths II
# Medium
# You are given an m x n integer array grid. There is a robot initially located at the top-left
# corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1]
# [n - 1]). The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes
# cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right
# corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 109.
from typing import List


# 2023-06-03 00:08:04
# original
# 2D dp
# time 54.33% space 55.13%
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        matrix = [[0] * n for _ in range(m)]
        matrix[-1][-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    continue
                if i + 1 != m and obstacleGrid[i + 1][j] != 1:
                    matrix[i][j] += matrix[i + 1][j]
                if j + 1 != n and obstacleGrid[i][j + 1] != 1:
                    matrix[i][j] += matrix[i][j + 1]
        return matrix[0][0]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))
print(s.uniquePathsWithObstacles([[0, 0], [0, 1]]))
print(s.uniquePathsWithObstacles([[0,0,1],[0,1,0],[0,1,0]]))
