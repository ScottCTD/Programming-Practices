# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        b, e = 0, len(nums)
        while b < e:
            m = (b + e) // 2
            n = nums[m]
            if n == target:
                b = e = m
                while b >= 0 and nums[b] == target:
                    b -= 1
                while e < l and nums[e] == target:
                    e += 1
                return [b + 1, e - 1]
            elif n > target:
                e = m
            else:
                b = m + 1
        return [-1, -1]
        

if __name__ == '__main__':
    s = Solution()

    print(s.searchRange([7,8,8,8,8,8,9], 7))