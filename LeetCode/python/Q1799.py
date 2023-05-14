# 1799. Maximize Score After N Operations
# You are given nums, an array of positive integers of size 2 * n.
# You must perform n operations on this array.
#
# In the ith operation (1-indexed), you will:
#
# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# Return the maximum score you can receive after performing n operations.
#
# The function gcd(x, y) is the greatest common divisor of x and y.

from collections import Counter
from math import gcd
from typing import List

# a previous bug: In the process of backtracking, I only added new things, forgot to utilize the
# things generated in the previous recursive call
# use a bit mask as a set to store if index is set or not
# backtrack bruteforce
# 2023-05-14 17:26:01
# half-original
# time 57.6 space 67.9%
# not optimal
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 2
        memo = {}
        def find_subsets(mask: int, k: int):
            if k == n:
                return 0
            if mask in memo:
                return memo[mask]
            max_score = 0
            for i in range(m):
                if mask >> i & 1:
                    continue
                mask |= 1 << i
                for j in range(i + 1, m):
                    if mask >> j & 1:
                        continue
                    mask |= 1 << j
                    score = (k + 1) * gcd(nums[i], nums[j])
                    score += find_subsets(mask, k + 1)
                    max_score = max(max_score, score)
                    mask ^= 1 << j
                mask ^= 1 << i
            memo[mask] = max_score
            return max_score

        return find_subsets(0, 0)


s = Solution()
print(s.maxScore([1, 2]))
print(s.maxScore([5, 5]))
print(s.maxScore([3, 4, 6, 8]))
print(s.maxScore([1, 2, 3, 4, 5, 6]))
print(s.maxScore([889509, 644676, 621999, 606262, 412720, 678593]))
print(s.maxScore([3, 6, 3, 6, 3, 6]))
