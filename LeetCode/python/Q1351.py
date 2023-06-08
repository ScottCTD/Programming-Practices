# 1351. Count Negative Numbers in a Sorted Matrix
# Easy
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
# return the number of negative numbers in grid.
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-07 21:15:41
# original
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    ans += n - j
                    break
        return ans

s = Solution()

