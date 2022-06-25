# 713. Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

from typing import List


class Solution:

    # learned
    # sliding window
    # if the product is greater then or equal to k, then we move b
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0
        result = 0
        n = len(nums)
        product = 1
        b = 0
        for e in range(n):
            product *= nums[e]
            while b <= e and product >= k:
                product //= nums[b]
                b += 1
            # the number of sub arrays is sum_{i=1}^n i, and we shouldn't add duplicates
            result += e - b + 1
        return result


s = Solution()
print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(s.numSubarrayProductLessThanK([1, 2, 3], 0))
print(s.numSubarrayProductLessThanK([2,3,4,5,6], 100))