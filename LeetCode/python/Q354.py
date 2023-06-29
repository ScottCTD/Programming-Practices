# 354. Russian Doll Envelopes
# Hard
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width
# and the height of an envelope.
#
# One envelope can fit into another if and only if both the width and height of one envelope are
# greater than the other envelope's width and height.
#
# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
#
# Note: You cannot rotate an envelope.
from typing import List
import bisect


# 2023-06-28 22:37:48
# original
# TLE: O(n^2)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes = sorted(envelopes)
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            max_len = 1
            ei = envelopes[i]
            for j in range(i - 1, -1, -1):
                ej = envelopes[j]
                if ei[1] > ej[1]:
                    max_len = max(max_len, dp[j] + 1)
                    dp[i] = max_len
            ans = max(ans, dp[i])
        return ans


# 2023-06-28 23:17:33
# learned
# people are very smart
class Solution2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda e: (e[0], -e[1]))
        # greedy list: the LIS so far
        # we want to minimize h but still keep increasing sequence
        res = []
        for _, h in envelopes:
            idx = bisect.bisect_left(res, h)
            # if greater than anyone, then add to the list
            if idx == len(res):
                res.append(h)
            else:
                # we know that width is increasing (not strictly), so we can always envelop
                # a previous one. We prefer one with smallest height to be added
                # so if width is the same, we replace the bigger height with the smaller height
                # if we have a smaller height, we can safely replace the previous one
                # because we can just "start over" the whole process
                # but we don't need to reset the res list because we already find len(res) LIS
                res[idx] = h
        return len(res)


s = Solution2()
# [[2, 3], [5, 4], [6, 7], [6, 4]]
print(s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))  # 3
print(s.maxEnvelopes([[1, 1], [1, 1], [1, 1]]))  # 1
# [[6, 10], [6, 1], [11, 14], [13, 2], [16, 14]]
print(s.maxEnvelopes([[6, 10], [11, 14], [6, 1], [16, 14], [13, 2]]))  # 3
print(s.maxEnvelopes(
    [[15, 8], [2, 20], [2, 14], [4, 17], [8, 19], [8, 9], [5, 7], [11, 19], [8, 11], [13, 11],
     [2, 13], [11, 19], [8, 11], [13, 11], [2, 13], [11, 19], [16, 1], [18, 13], [14, 17],
     [18, 19]]))  # 5
