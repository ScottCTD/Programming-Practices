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
# count the # of ones in binary representation
#
# 3 times
#
# we need 2 bits 00, 01, 10, 11
# we can select only 3 (00, 10, 01)
#
# use two ints to represent the count
#
# i1 and i2, for 01, i1 corresponds to 0, i2 corresponds to 1
#
# if i1 and input is different, then we want to and with ~i2 to get the answer
#
# i1 = (i1 ^ input) & ~i2
# i2 = (i2 ^ input) & ~i1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i1, i2 = 0, 0
        for num in nums:
            i1 = (i1 ^ num) & ~i2
            i2 = (i2 ^ num) & ~i1
        return i1


s = Solution()
print(s.singleNumber([1, 1, 1, 2]))
