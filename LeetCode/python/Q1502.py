# 1502. Can Make Arithmetic Progression From Sequence
# Easy
# A sequence of numbers is called an arithmetic progression if the difference between any two
# consecutive elements is the same.
#
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic
# progression. Otherwise, return false.
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-05 20:46:46
# original
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        d = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1]  != d:
                return False
        return True


s = Solution()

