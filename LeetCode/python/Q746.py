# 746. Min Cost Climbing Stairs
# Easy
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
from typing import List


# 2023-06-05 16:19:38
# original
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp = [0] * (n + 1)
        # dp[-2] = cost[-1]
        dp2 = 0
        dp1 = cost[-1]
        dp0 = 0
        for i in range(n - 2, -1, -1):
            # dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
            dp0 = cost[i] + min(dp1, dp2)
            dp2, dp1 = dp1, dp0
        # dp2 because swap
        return min(dp0, dp2)


s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))
