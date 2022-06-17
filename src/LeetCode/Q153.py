# 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ = nums[0]
        b, e = 0, len(nums)
        while b < e:
            m = (b + e) // 2
            n = nums[m]
            l, r = nums[b], nums[e - 1]
            # left part is sorted
            if n > r:
                min_ = min(min_, l)
                b = m + 1
            # right is sorted
            else:
                min_ = min(min_, n)
                e = m
        return min_


s = Solution()
print(s.findMin([90, 10, 20, 30]))
print(s.findMin([4,5,1,2,3]))
