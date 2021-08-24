# 66. Plus One
# Given a non-empty array of decimal digits representing a non-negative integer,
# increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

from typing import List


class Solution:

    # Not Original
    # 97.87%
    # Time O(n)
    # Space O(1)
    def plusOne2(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        if digits[0] == 0:
            return [1] + digits

    # Original
    # 79.53%
    # Time O(n)
    # Space O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[n - 1] += 1
        if digits[n - 1] >= 10:
            digits[n - 1] = 0
            if n == 1:
                digits.insert(0, 1)
            for i in range(n - 2, -1, -1):
                digits[i] += 1
                if digits[i] >= 10:
                    digits[i] = 0
                    if i == 0:
                        digits.insert(0, 1)
                else:
                    break
        return digits


print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne([9]))
print(Solution().plusOne([9, 8, 9]))
