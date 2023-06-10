
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-10 12:22:23
# original
class Solution:
    def isFascinating(self, n: int) -> bool:
        a = [False] * 9
        ns = str(n)
        newn_s = ns + str(n * 2) + str(n * 3)
        for num in newn_s:
            if num == '0':
                return False
            if a[int(num) - 1]:
                return False
            a[int(num) - 1] = True
        return all(a)

s = Solution()
print(s.isFascinating(267))
