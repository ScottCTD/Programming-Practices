# 31. Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is impossible, it must rearrange it to the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

from typing import List


class Solution:

    # 2022/01/17 Half-Original Scott 2h+
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # I got into a wrong understanding of this question and that's why I spent lots of time.
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i >= 0 and nums[i] <= nums[i - 1]:
            i -= 1
        i -= 1
        if i >= 0:
            num = nums[i]
            j = n - 1
            while j > i and nums[j] <= num:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        print(nums)


if __name__ == '__main__':
    s = Solution()

    s.nextPermutation([2, 3, 1])  # 312
    s.nextPermutation([1, 2, 3])  # 132
    s.nextPermutation([3, 2, 1])  # 123
    s.nextPermutation([1, 1, 5])  # 151
    s.nextPermutation([1, 3, 5, 2, 1, 4, 3])  # 1352314
    s.nextPermutation([1, 8, 7, 6, 5, 4, 3])
    s.nextPermutation([3, 8, 7, 6, 5, 4, 1])
    s.nextPermutation([1, 8, 7, 6, 2, 4, 9])
    s.nextPermutation([1, 8, 2, 6, 5, 4, 3])
    s.nextPermutation([4, 4, 4, 5, 4, 3])
    s.nextPermutation([4, 2, 0, 2, 3, 2, 0])  # [4,2,0,3,0,2,2]
