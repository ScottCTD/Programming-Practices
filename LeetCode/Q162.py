# 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

from typing import List


class Solution:

    # not original
    # i cannot do this
    # a smart usage of binary search
    # the key is to find the pattern and then shrink the input until only 1 element left inside [b, e]
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        b, e = 0, n - 1
        while b < e:
            m = (b + e) // 2
            num = nums[m]
            if num < nums[m + 1]:
                b = m + 1
            else:
                e = m
        return b


s = Solution()
print(s.findPeakElement([1,2,3,4]))
print(s.findPeakElement([4,3,2,1]))
