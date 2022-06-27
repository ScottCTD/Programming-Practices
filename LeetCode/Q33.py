# 33. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b, e = 0, len(nums)
        while b < e:
            m = (b + e) // 2
            mn = nums[m]
            if target == mn:
                return m
            # if left is sorted
            # in some cases nums[m] may equal to nums[e - 1]
            if mn >= nums[e - 1]:
                # if target in left
                # corner cases that m == e - 1 because our m is always rightward
                if nums[b] <= target < mn or m == e - 1:
                    e = m
                else:
                    b = m + 1
            # if right is sorted
            elif mn < nums[e - 1]:
                if mn < target <= nums[e - 1]:
                    b = m + 1
                else:
                    e = m
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 3))
    print(s.search([1,3], 1))
    print(s.search([1,3], 3))
    print(s.search([3, 1], 3))