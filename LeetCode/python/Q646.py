# 646. Maximum Length of Pair Chain
# Medium
# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
#
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this
# fashion.
#
# Return the length longest chain which can be formed.
#
# You do not need to use up all the given intervals. You can select pairs in any order.
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs = sorted(pairs, key=lambda e: e[0])
        # dp[i] means the answer ending at i
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            max_len = 1
            for j in range(i - 1, -1, -1):
                if pairs[i][0] > pairs[j][1]:
                    max_len = max(max_len, dp[j] + 1)
                    dp[i] = max_len
            ans = max(ans, max_len)
        return ans


s = Solution()
print(s.findLongestChain([[1, 2], [2, 3], [3, 4]]))  # 2
print(s.findLongestChain([[1, 2], [7, 8], [4, 5]]))  # 3
print(s.findLongestChain([[1, 2]]))  # 1
