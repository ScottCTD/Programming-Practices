# 1802. Maximum Value at a Given Index in a Bounded Array
# Medium
# You are given three positive integers: n, index, and maxSum. You want to construct an array nums
# (0-indexed) that satisfies the following conditions:
#
# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.
# Return nums[index] of the constructed array.
#
# Note that abs(x) equals x if x >= 0, and -x otherwise.
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-09 22:52:44
# partially original
# binary search to optimize the resutls
# greedy and math to calculate the array sum
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # [i:j]
        i, j = 1, maxSum - n + 2
        ans = 1
        while i < j:
            m = (i + j) >> 1
            # calculate sum
            s = m
            lt = index - m + 1
            t = ((m - 1) * m) >> 1
            if lt >= 0:
                s += t + lt
            else:
                s += t - (((-lt + 1) * -lt) >> 1)
            rt = n - index - m
            if rt >= 0:
                s += t + rt
            else:
                s += t - (((-rt + 1) * -rt) >> 1)
            if s == maxSum:
                return m
            elif s < maxSum:
                i = m + 1
                ans = m
            else:
                j = m
        return ans


s = Solution()
print(s.maxValue(4, 2, 6))
print(s.maxValue(6, 1, 10))
print(s.maxValue(7, 0, 7))
print(s.maxValue(1, 0, 7))
