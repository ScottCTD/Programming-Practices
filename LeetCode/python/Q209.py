# 209. Minimum Size Subarray Sum
# Medium
# Given an array of positive integers nums and a positive integer target, return the minimal length
# of a subarray whose sum is greater than or equal to target. If there is no such subarray,
# return 0 instead.
from typing import List


# 2023-07-06 00:00:51
# original
# sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        ans = n + 1
        current_sum = 0
        for i in range(n):
            current_sum += nums[i]
            while current_sum >= target:
                ans = min(ans, i - start + 1)
                current_sum -= nums[start]
                start += 1
        return min(ans, n - start + 1) if ans != n + 1 else 0


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
print(s.minSubArrayLen(4, [1, 4, 4]))  # 1
print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0
print(s.minSubArrayLen(80, [10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8]))  # 6
