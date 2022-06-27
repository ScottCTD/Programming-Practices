# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

from typing import List


class Solution:

    # 2022/01/31 Scott
    # Time Complexity: O(n) 32.75%
    # Space Complexity: O(n) 5.15%
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [num ** 2 for num in nums]
        n = len(nums)
        result = []
        left, right = 0, 1
        while right < n and nums[right] < 0:
            right += 1
            left += 1
        if right == n:
            return [nums[i] ** 2 for i in range(n - 1, -1, -1)]
        while right < n and left >= 0:
            l = abs(nums[left])
            r = abs(nums[right])
            if l < r:
                result.append(l ** 2)
                left -= 1
            elif l > r:
                result.append(r ** 2)
                right += 1
            else:
                result.extend([l ** 2, r ** 2])
                right += 1
                left -= 1
        if right <= n - 1:
            result.extend(nums[i] ** 2 for i in range(right, n))
        elif left >= 0:
            result.extend(nums[i] ** 2 for i in range(left, -1, -1))
        return result



if __name__ == '__main__':
    s = Solution()

    print(s.sortedSquares([-4,-1,0,3,10]))
    print(s.sortedSquares([-7,-3,2,3,11]))
    print(s.sortedSquares([-10, -9, -8, -7, -6, -5]))
    print(s.sortedSquares([-10,-8,-5,-4,-3,2]))
