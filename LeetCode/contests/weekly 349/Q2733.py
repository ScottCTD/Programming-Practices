from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-11 01:07:31
# original
# could easily be optimized, but not necessary
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums = set(nums)
        min_ = min(nums)
        max_ = max(nums)
        nums.remove(min_)
        if max_ in nums:
            nums.remove(max_)
        if len(nums) == 0:
            return -1
        return nums.pop()


s = Solution()

