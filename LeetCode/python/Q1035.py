# 1035. Uncrossed Lines
# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2
# (in the order they are given) on two separate horizontal lines.
#
# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j]
# such that:
# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints
# (i.e., each number can only belong to one connecting line).
#
# Return the maximum number of connecting lines we can draw in this way.

from typing import List


# 2023-05-11 14:13:40
# partially original
# top-down dp with memoization
# time 24.93% space 22.83%
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        memo = [[-1] * m for _ in range(n)]

        def f(i, j):
            if i == -1 or j == -1:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if nums1[i] == nums2[j]:
                memo[i][j] = 1 + f(i - 1, j - 1)
            else:
                memo[i][j] = max(f(i - 1, j), f(i, j - 1))
            return memo[i][j]

        return f(n - 1, m - 1)


# 2023-05-11 14:24:38
# learned
# bottom-up dp
# time 57.48% space 29.13%
class Solution2:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        memo = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
        return memo[n][m]


s = Solution2()
print(s.maxUncrossedLines([1, 4, 2], [1, 2, 4]))
