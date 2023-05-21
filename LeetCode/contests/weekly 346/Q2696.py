

from typing import List, Optional
from collections import deque, defaultdict


# 2023-05-21 00:08:13
# original
class Solution:
    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
            s = s.replace('AB', '')
            s = s.replace('CD', '')
        return len(s)

s = Solution()

