# 673. Number of Longest Increasing Subsequence
# Medium
# Given an integer array nums, return the number of longest increasing subsequences.
#
# Notice that the sequence has to be strictly increasing.
from typing import List


# 2023-06-20 13:15:46
# learned
# dp
# time O(n^2) 81.42% space O(n) 70.4%
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] = the length of the LIS of nums[:i + 1]
        dp = [1] * n
        # count[i] = the number of LIS in nums[:i + 1]
        count = [1] * n
        max_len = 1
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                # if forms an increasing sequence
                if nums[j] < nums[i]:
                    # current increasing sequence length
                    l = dp[j] + 1
                    if l > dp[i]:  # longer sequence: we can construct count[j] + 1 such sequence
                        dp[i] = l
                        count[i] = count[j]
                    elif l == dp[i]:  # if same length
                        # then we know that count[i] should include those in count[j]
                        count[i] += count[j]
            max_len = max(max_len, dp[i])
        return sum(count[i] for i in range(n) if dp[i] == max_len)


s = Solution()
print(s.findNumberOfLIS([1, 3, 5, 4, 7]))
print(s.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
print(s.findNumberOfLIS([1, 1, 1, 2, 2, 2, 3, 3, 3]))
