# 1027. Longest Arithmetic Subsequence
#
# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
#
# Note that:
#
# A subsequence is an array that can be derived from another array by deleting some or no elements
# without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value
# (for 0 <= i < seq.length - 1).
from typing import List, Optional
from collections import deque, defaultdict
import heapq


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(lambda: 2)
        ans = 2
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                d = nums[i] - nums[j]
                if (j, d) in dp:
                    dp[(i, d)] = max(dp[(i, d)], dp[(j, d)] + 1)
                ans = max(ans, dp[(i, d)])
        return ans


s = Solution()
print(s.longestArithSeqLength([3, 6, 9, 12]))
print(s.longestArithSeqLength([9, 4, 7, 2, 10]))
print(s.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))
print(s.longestArithSeqLength([1, 1, 1, 1]))
print(s.longestArithSeqLength(
    [22, 8, 57, 41, 36, 46, 42, 28, 42, 14, 9, 43, 27, 51, 0, 0, 38, 50, 31, 60, 29, 31, 20, 23, 37,
     53, 27, 1, 47, 42, 28, 31, 10, 35, 39, 12, 15, 6, 35, 31, 45, 21, 30, 19, 5, 5, 4, 18, 38, 51,
     10, 7, 20, 38, 28, 53, 15, 55, 60, 56, 43, 48, 34, 53, 54, 55, 14, 9, 56, 52]))
