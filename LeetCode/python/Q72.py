# 72. Edit Distance
# Hard
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
from typing import List, Optional
from collections import deque, defaultdict
import heapq

# 2023-06-05 16:02:15
# learned
# bottom-up dp
# the key is to understand how to perform each operation on a smaller level
# how to break the problem into sub-problems?
# we can use some simpler example to explore some ideas
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        # n1 * n2
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            dp[i][0] = i
        for j in range(1, n2 + 1):
            dp[0][j] = j
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        # add a new one
                        dp[i][j - 1],
                        # delete
                        dp[i - 1][j],
                        # modify
                        dp[i - 1][j - 1]
                    ) + 1
        return dp[n1][n2]


s = Solution()
print(s.minDistance('horse', 'ros'))
print(s.minDistance('intention', 'execution'))
