

from typing import List, Optional
from collections import deque, defaultdict
from math import gcd


# 2023-05-27 12:06:07
# original
# TLE
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        graph = {}
        for i in range(n):
            for j in range(i + 1, n):
                v, u = nums[i], nums[j]
                if gcd(v, u) > 1:
                    if v in graph:
                        graph[v].append(u)
                    else:
                        graph[v] = [u]
                    if u in graph:
                        graph[u].append(v)
                    else:
                        graph[u] = [v]
        # check if the graph is connected
        visited = set()
        queue = deque()
        queue.append(nums[0])
        while queue:
            v = queue.popleft()
            visited.add(v)
            for child in graph[v]:
                if child not in visited:
                    queue.append(child)
        return visited == set(nums)


s = Solution()
print(s.canTraverseAllPairs([2,3,6]))
print(s.canTraverseAllPairs([3, 9, 5]))
import random
a = [random.randint(1, 10 ** 5) for _ in range(10 ** 5)]
print(a)
print(s.canTraverseAllPairs(a))
