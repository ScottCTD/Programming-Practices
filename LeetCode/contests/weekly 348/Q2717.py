
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-03 23:40:16
# original
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(1)
        # try two
        a = nums.copy()
        count = 0
        while a[0] != 1:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
            count += 1
        j = a.index(n)
        while a[-1] != n:
            a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
            count += 1

        a = nums.copy()
        count2 = 0
        j = nums.index(n)
        while a[-1] != n:
            a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
            count2 += 1
        i = a.index(1)
        while a[0] != 1:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
            count2 += 1
        return min(count, count2)


s = Solution()
print(s.semiOrderedPermutation([2,1,4,3]))
print(s.semiOrderedPermutation([2,4,1,3]))
