# 74. Search a 2D Matrix
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

from typing import List


class Solution:

    # original
    # double binary search
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b, m, e = 0, 0, len(matrix)
        while b < e:
            m = (b + e) // 2
            l, r = matrix[m][0], matrix[m][-1]
            if l == target or r == target:
                return True
            # in range
            if l < target < r:
                break
            elif target > r:
                b = m + 1
            else:
                e = m
        if b >= e:
            return False
        nums = matrix[m]
        b, e = 0, len(nums)
        while b < e:
            m = (b + e) // 2
            n = nums[m]
            if n == target:
                return True
            elif target > n:
                b = m + 1
            else:
                e = m
        return False
    
    # not original
    # pretty smart
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        row, column = 0, len(matrix[0]) - 1
        while row < n and column >= 0:
            a = matrix[row][column]
            if a == target:
                return True
            elif target > a:
                row += 1
            else:
                column -= 1
        return False