# 2656. Maximum Sum With Exactly K Elements
# You are given a 0-indexed integer array nums and an integer k.
# Your task is to perform the following operation exactly k times in order to maximize your score:
#
# Select an element m from nums.
# Remove the selected element m from the array.
# Add a new element with a value of m + 1 to the array.
# Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.

from typing import List

# 2023-05-13 00:03:00
# contest question
# original
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        sum_ = 0
        for i in range(k):
            sum_ += max_ + i
        return sum_