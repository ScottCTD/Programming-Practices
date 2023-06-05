# 198. House Robber
# Medium
# You are a professional robber planning to rob houses along a street. Each house has a certain
# amount of money stashed, the only constraint stopping you from robbing each of them is that
# adjacent houses have security systems connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum
# amount of money you can rob tonight without alerting the police.
from typing import List


# 2023-06-05 16:40:01
# original
# dp with space optimization
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # dp = [0] * n
        # dp[-1], dp[-2] = nums[-1], max(nums[-1], nums[-2])
        dp2, dp1 = nums[-1], max(nums[-1], nums[-2])
        dp0 = dp1
        for i in range(n - 3, -1, -1):
            # dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            dp0 = max(nums[i] + dp2, dp1)
            dp2, dp1 = dp1, dp0
        return dp0


s = Solution()
print(s.rob([1, 3, 1]))
print(s.rob([4, 1, 2, 7, 5, 3, 1]))  # 14
print(s.rob([1, 1]))  # 14
