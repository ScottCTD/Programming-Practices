# 1547. Minimum Cost to Cut a Stick
# Hard
# Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of
# length 6 is labelled as follows:
# Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.
#
# You should perform the cuts in order, you can change the order of the cuts as you wish.
#
# The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of
# all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their
# lengths is the length of the stick before the cut). Please refer to the first example for
# a better explanation.
#
# Return the minimum total cost of the cuts.

from typing import List

class Solution:

    # 2023-05-28 01:08:24
    # learned
    # bottom-up dp
    # dp[i][j] represents the minimum cost of cutting from new_cuts[i] to new_cuts[j]
    def minCost(self, n: int, cuts: List[int]) -> int:
        new_cuts = [0] + sorted(cuts) + [n]
        m = len(new_cuts)
        dp = [[0] * (m) for _ in range(m)]
        for d in range(2, m):
            for l in range(m - d):
                r = l + d
                fee = new_cuts[r] - new_cuts[l]
                cost = dp[l][l + 1] + dp[l + 1][r] + fee
                for mid in range(l + 2, r):
                    cost = min(cost, dp[l][mid] + dp[mid][r] + fee)
                dp[l][r] = cost
        return dp[0][-1]
