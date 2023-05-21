

from typing import List, Optional
from collections import deque, defaultdict


# 2023-05-21 00:08:19
# original
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        a = list(s)
        for i in range(n // 2):
            c1, c2 = a[i], a[-i - 1]
            if c1 != c2:
                if c1 < c2:
                    a[-i - 1] = c1
                else:
                    a[i] = c2
        return ''.join(a)

s = Solution()

