# 1218. Longest Arithmetic Subsequence of Given Difference
# Medium
# Given an integer array arr and an integer difference, return the length of the longest subsequence
# in arr which is an arithmetic sequence such that the difference between adjacent elements in the
# subsequence equals difference.
#
# A subsequence is a sequence that can be derived from arr by deleting some or no elements without
# changing the order of the remaining elements.
from typing import List


# 2023-06-27 11:53:33
# original
# not so efficient
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        ans = 1
        for i in range(n):
            e = arr[i]
            t = e - difference
            if t in dp:
                # this max is probably useless
                dp[e] = max(dp.get(e, 1), dp[t] + 1)
            if e not in dp:
                dp[e] = 1
            ans = max(ans, dp[e])
        return ans


# 2023-06-27 11:56:57
# learned
# optimized version of my solution
class Solution2:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        for e in arr:
            t = e - difference
            dp[e] = dp.get(t, 0) + 1
            ans = max(ans, dp[e])
        return ans


s = Solution()
print(s.longestSubsequence([1, 2, 3, 4], 1))  # 4
print(s.longestSubsequence([1, 3, 5, 7], 1))  # 1
print(s.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))  # 4
print(s.longestSubsequence([4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8], 0))  # 2
