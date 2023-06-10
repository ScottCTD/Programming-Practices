
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# 2023-06-10 12:22:12
# original
# sliding window
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        r = -1
        i = 0
        j = 1
        while j < n:
            if s[j] == s[j - 1]:
                if r == -1:
                    r = j
                    j += 1
                else:
                    ans = max(ans, j - i)
                    i = r
                    r = -1
            else:
                j += 1
        ans = max(ans, j - i)
        return ans if ans != 0 else n


s = Solution()
print(s.longestSemiRepetitiveSubstring("52233"))
print(s.longestSemiRepetitiveSubstring("1111111"))
print(s.longestSemiRepetitiveSubstring("5494"))
print(s.longestSemiRepetitiveSubstring("0001"))
