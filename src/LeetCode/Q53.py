# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Scott 2021/08/24

from typing import List

class Solution:

    # Original
    # 5.75%
    # Brute Force O(n^2)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        for i in range(n):
            sum = nums[i]
            if sum > result:
                    result = sum
            for j in range(i + 1, n):
                sum += nums[j]
                if sum > result:
                    result = sum
        return result


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1]))
    print(Solution().maxSubArray([-1,0,-2]))