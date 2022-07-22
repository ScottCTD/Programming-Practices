# 213. House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
# rob tonight without alerting the police.

from typing import List


class Solution:

    # 2022/07/22
    # dynamic programming
    # state transition function is dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    #                                          rob i,               not rob
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        result = 0
        dp = [0] * n
        # rob the first one, so that cannot rob n - 1th
        dp[0], dp[1] = nums[0], nums[0]
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        result = dp[n - 2]
        dp[0], dp[1] = 0, nums[1]
        # rob the second one
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        result = max(result, dp[n - 1])
        return result

s = Solution()

print(s.rob([2, 3, 2])) # 3
print(s.rob([1,2,3,1])) # 4
print(s.rob([1,2,3])) # 3
print(s.rob([1,3,1,3,100])) # 103
