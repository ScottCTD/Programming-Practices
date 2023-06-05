# 516. Longest Palindromic Subsequence
# Medium
# Given a string s, find the longest palindromic subsequence's length in s.
#
# A subsequence is a sequence that can be derived from another sequence by deleting some or no
# elements without changing the order of the remaining elements.
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-05 01:24:24
# partially original (learned some)
# 2D dp
# time 42.1 space 50.33
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # fill in length 1 and 2
        for i in range(n - 1):
            dp[i][i] = 1
            dp[i][i + 1] = 1
            if s[i] == s[i + 1]:
                dp[i][i + 1] += 1
        dp[-1][-1] = 1
        # fill remaining
        for l in range(2, n):
            for i in range(n - l):
                j = i + l
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


s = Solution()
print(s.longestPalindromeSubseq("bbbab"))
print(s.longestPalindromeSubseq("cbbd"))
print(s.longestPalindromeSubseq("abcdef"))
print(s.longestPalindromeSubseq("abcabcabcabc"))
