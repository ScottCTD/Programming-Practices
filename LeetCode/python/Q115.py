# 115. Distinct Subsequences
# Hard
# Given two strings s and t, return the number of distinct
# subsequences of s which equals t.
#
# The test cases are generated so that the answer fits on a 32-bit signed integer.

# 2023-06-06 01:19:11
# learned
# 2D dp
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # idea: dp[i][j] = # of distinct subsequences of s[i:] which equals t[j:]
        # base case: dp[i][m] = 1
        # the answer is dp[0][0]
        n, m = len(s), len(t)
        if n < m:
            return 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    #          with s[i]          without s[i]
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    #          the only case is without s[i]
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]


# 2023-06-06 01:24:45
# learned
# 1D dp, very smart
# the best solution
class Solution2:

    def numDistinct(self, s: str, t: str) -> int:
        # idea: dp[i] is the # of subsequences of s that equals to t[:i]
        n, m = len(s), len(t)
        dp = [1] + [0] * m
        for i in range(n - m + 1):
            window = s[i:i + m]
            for j in range(m):
                if window[j] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]


s = Solution2()
print(s.numDistinct('rabbbit', 'rabbit'))
print(s.numDistinct('babgbag', 'bag'))
