# 2462. Total Cost to Hire K Workers
# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
#
# You are also given two integers k and candidates. We want to hire exactly k workers according to
# the following rules:
#
# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates
# workers or the last candidates workers. Break the tie by the smallest index.
# For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session,
# we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
# In the second hiring session, we will choose 1st worker because they have the same lowest cost as
# 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be
# changed in the process.
# If there are fewer than candidates workers remaining, choose the worker with the lowest cost among
# them. Break the tie by the smallest index.
# A worker can only be chosen once.
# Return the total cost to hire exactly k workers.
import heapq
from typing import List


# 2023-06-25 22:31:57
# original
# not very efficient
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates << 1 >= n:
            # print(heapq.nsmallest(k, costs))
            return sum(heapq.nsmallest(k, costs))
        c = [(c, i) for i, c in enumerate(costs)]
        i, j = candidates, n - candidates - 1
        h1, h2 = c[:candidates], c[-candidates:]
        heapq.heapify(h1)
        heapq.heapify(h2)
        ans = 0
        for _ in range(k):
            if h1[0][0] <= h2[0][0]:
                ans += heapq.heappop(h1)[0]
                if i <= j:
                    heapq.heappush(h1, c[i])
                    i += 1
                if not h1:
                    h1.append((100001, 0))
            else:
                ans += heapq.heappop(h2)[0]
                if i <= j:
                    heapq.heappush(h2, c[j])
                    j -= 1
                if not h2:
                    h2.append((100001, 0))
        return ans


# 2023-06-25 23:10:35
# learned
# using one heap
# a bit better
class Solution2:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates << 1 >= n:
            return sum(heapq.nsmallest(k, costs))
        c = [(c, i) for i, c in enumerate(costs)]
        h = c[:candidates] + c[-candidates:]
        heapq.heapify(h)
        i, j = candidates, n - candidates - 1
        ans = 0
        for _ in range(k):
            a, idx = heapq.heappop(h)
            ans += a
            if i > j:
                continue
            if idx < i:
                heapq.heappush(h, c[i])
                i += 1
            else:
                heapq.heappush(h, c[j])
                j -= 1
        return ans


s = Solution2()
print(s.totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4))  # 11
print(s.totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 8, 2))  # 69
print(s.totalCost([1, 2, 4, 1], 3, 3))  # 4
print(s.totalCost([3, 2, 7, 7, 1, 2], 5, 2))  # 15
print(s.totalCost([2, 1, 1], 3, 1))  # 4
