# 435. Non-overlapping Intervals
# Medium
# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest 
# of the intervals non-overlapping.
from typing import List


# Greedy
# Time: O(nlogn)
# Space: O(1)
class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda e: e[1])
        r = 0
        ps, pf = intervals[0]
        for i in range(1, n):
            s, f = intervals[i]
            if pf > s:
                r += 1
            else:
                ps, pf = s, f
        return r


s = Solution()
print(s.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]))
