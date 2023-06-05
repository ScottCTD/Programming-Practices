
from typing import List, Optional
from collections import deque, defaultdict
import heapq

# 2023-06-03 23:40:03
# original
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s = set(s)
        return len(s)

s = Solution()
