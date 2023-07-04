# 137. Single Number II
# Medium
# Given an integer array nums where every element appears three times except for one, which appears
# exactly once. Find the single element and return it.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
from typing import List


# 2023-07-04 14:02:52
# learned
# very smart bit manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i1, i2 = 0, 0
        for num in nums:
            i1 = (i1 ^ num) & ~i2
            i2 = (i2 ^ num) & ~i1
        return i1


s = Solution()
print(s.singleNumber([1, 1, 1, 2]))
