# 5. Longest Palindromic Substring
# Medium
# Given a string s, return the longest palindromic substring in s.
from typing import List, Optional
from collections import deque, defaultdict
import heapq

# TODO: more solutions

# 2023-06-03 01:32:14
# learned
# dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        max_str = s[0]
        for i in range(n):
            dp[i][i] = True
            if i + 1 == n:
                continue
            dp[i][i + 1] = s[i] == s[i + 1]
            if dp[i][i + 1]:
                max_len = 2
                max_str = s[i:i + 2]
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j] and j - i + 1 > max_len:
                        max_len = j - i + 1
                        max_str = s[i:j + 1]
                else:
                    dp[i][j] = False
        return max_str


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("aacabdkacaa"))
print(s.longestPalindrome("aaaaa"))

