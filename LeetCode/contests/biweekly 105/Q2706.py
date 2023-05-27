

from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-05-27 12:05:48
# original
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        r = money - heapq.heappop(prices) - heapq.heappop(prices)
        if r >= 0:
            return r
        else:
            return money

s = Solution()
print(s.buyChoco([1,2,2], 3))
