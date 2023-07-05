# 1493. Longest Subarray of 1's After Deleting One Element
# Medium
# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.
from typing import List


# 2023-07-04 23:55:31
# learned
# I'm stupid.
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        zeros = 0
        ans = 0
        for i in range(n):
            zeros += int(nums[i] == 0)
            while zeros > 1:
                zeros -= int(nums[s] == 0)
                s += 1
            ans = max(ans, i - s)
        return ans


s = Solution()
print(s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
print(s.longestSubarray([1, 1, 0, 1]))  # 3
print(s.longestSubarray([1, 1, 1]))  # 2
print(s.longestSubarray([1, 0, 1, 0, 1]))  # 2
print(s.longestSubarray([1, 0, 0, 1]))  # 1
print(s.longestSubarray([1, 0, 1, 0, 1, 0]))  # 2
print(s.longestSubarray([1, 1, 1, 0, 0, 0, 1, 1, 1, 1]))  # 4
