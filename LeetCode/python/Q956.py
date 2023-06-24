# 956. Tallest Billboard
# Hard
# You are installing a billboard and want it to have the largest height.
# The billboard will have two steel supports,
# one on each side. Each steel support must be an equal height.
#
# You are given a collection of rods that can be welded together.
# For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a
# support of length 6.
#
# Return the largest possible height of your billboard installation. If you cannot support the
# billboard, return 0.
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-24 14:46:15
# learned
# very smart use of dp
# wow bro I'm so DUMB
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[diff] = taller
        dp = {0: 0}
        n = len(rods)
        for i in range(n):
            new_dp = dp.copy()
            l = rods[i]
            for d, t in dp.items():
                s = t - d
                # 1. add to taller
                new_t = t + l
                new_d = new_t - s
                new_dp[new_d] = max(new_dp.get(new_d, 0), new_t)
                # 2. add to shorter
                new_s = s + l
                new_d = abs(t - new_s)
                new_dp[new_d] = max(new_dp.get(new_d, 0), max(new_s, t))
            dp = new_dp
        return dp[0]


s = Solution()
print(s.tallestBillboard([1, 2, 3, 6]))
print(s.tallestBillboard([1, 2, 3, 4, 5, 6]))
