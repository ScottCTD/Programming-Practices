# 120. Triangle
# Medium
# 8.2K
# 484
# Companies
# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More formally,
# if you are on index i on the current row,
# you may move to either index i or index i + 1 on the next row.
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-03 00:13:42
# original
# dp
# time 46.45% space 57.49
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        for i in range(rows - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(s.minimumTotal([[-10]]))

