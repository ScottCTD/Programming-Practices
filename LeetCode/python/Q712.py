# 712. Minimum ASCII Delete Sum for Two Strings
# Medium
# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two
# strings equal.
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-05 23:52:55
# original
# 2D dp
# could do some space optimizations
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        ord_s1, ord_s2 = [0] * n1, [0] * n2
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            ord_s1[i - 1] = ord(s1[i - 1])
            dp[i][0] = dp[i - 1][0] + ord_s1[i - 1]
        for j in range(1, n2 + 1):
            ord_s2[j - 1] = ord(s2[j - 1])
            dp[0][j] = dp[0][j - 1] + ord_s2[j - 1]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord_s1[i - 1],
                        dp[i][j - 1] + ord_s2[j - 1],
                        dp[i - 1][j - 1] + ord_s1[i - 1] + ord_s2[j - 1]
                    )
        return dp[-1][-1]


s = Solution()
print(s.minimumDeleteSum('sea', 'eat'))
print(s.minimumDeleteSum('delete', 'leet'))
