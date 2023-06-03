# 931. Minimum Falling Path Sum
# Medium
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix
#
# A falling path starts at any element in the first row and chooses the element in the next row that
# is either directly below or diagonally left/right. Specifically, the next element from position
# (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-03 00:47:39
# original
# dp
# time 48.67% space 22.62%
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(n - 2, -1, -1):
            for j in range(n):
                matrix[i][j] += min(matrix[i + 1][max(0, j - 1)], matrix[i + 1][j],
                                    matrix[i + 1][min(n - 1, j + 1)])
        return min(matrix[0])


s = Solution()
print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
