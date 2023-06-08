# 300. Longest Increasing Subsequence
# Medium
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
from typing import List


# 2023-06-07 23:47:40
# learned
# dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            max_len = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    max_len = max(max_len, dp[j])
                    dp[i] = max_len + 1
            ans = max(ans, dp[i])
        return ans


# TODO: another solution with greedy and binary search


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
print(s.lengthOfLIS([0]))
