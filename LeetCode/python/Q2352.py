# 2352. Equal Row and Column Pairs
# Medium
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri
# and column cj are equal.
#
# A row and column pair is considered equal if they contain the same elements in the same order
# (i.e., an equal array).
from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq


# 2023-06-12 23:04:59
# almost original
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        freq = Counter(tuple(e) for e in grid)
        ans = 0
        for i in range(n):
            ans += freq[tuple(grid[j][i] for j in range(n))]
        return ans


s = Solution()


