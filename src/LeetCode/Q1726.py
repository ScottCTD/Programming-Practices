# 1726. Tuple with Same Product
# Given an array nums of distinct positive integers,
# return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c,
# and d are elements of nums, and a != b != c != d.
# Scott 2021/08/13

from typing import List


class Solution:

    # Not original
    # 94.05%
    def tupleSameProduct(self, nums: List[int]) -> int:
        m = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = nums[i] * nums[j]
                if k in m:
                    m[k] += 1
                else:
                    m[k] = 1
        result = 0
        for key in m:
            # This step confused me
            result += m[key] * (m[key] - 1) // 2
        return result * 8


if __name__ == '__main__':
    print(Solution().tupleSameProduct([2, 3, 4, 6]) == 8)
    print(Solution().tupleSameProduct([1, 2, 4, 5, 10]) == 16)
    print(Solution().tupleSameProduct([2, 3, 4, 6, 8, 12]) == 40)
