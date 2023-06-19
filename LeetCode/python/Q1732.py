# 1732. Find the Highest Altitude
# Easy
# 2.2K
# 184
# Companies
# There is a biker going on a road trip. The road trip consists of n + 1 points at different
# altitudes. The biker starts his trip on point 0 with altitude equal 0.
#
# You are given an integer array gain of length n where gain[i] is the net gain in altitude
# between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
from typing import List


# 2023-06-19 15:14:16
# original
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = gain[0]
        ans = max(0, a)
        for i in range(1, len(gain)):
            a += gain[i]
            if a > ans:
                ans = a
        return ans


s = Solution()
