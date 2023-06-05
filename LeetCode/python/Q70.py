# 70. Climbing Stairs
# Easy
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# 2023-06-05 15:03:29
# original
# dp
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n
        dp[-1] = 1
        dp[-2] = 2
        for i in range(n - 3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]


