# 934. Shortest Bridge
# Medium
# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
#
# An island is a 4-directionally connected group of 1's not connected to any other 1's.
# There are exactly two islands in grid.
#
# You may change 0's to 1's to connect the two islands to form one island.
#
# Return the smallest number of 0's you must flip to connect the two islands.

from typing import List


# 2023-05-20 21:59:21
# original + a tiny bit implementation inspired
# DFS + BFS
# time 82.98% O(n^2) space 40.56% O(n^2)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # use DFS to get any island
        # the island is a graph with each node has "0" as neighbors (if exist)
        # we can use -1 to denote the island we found
        n = len(grid)
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = []

        def dfs(i, j):
            grid[i][j] = -1
            queue.append((i, j))
            for d0, d1 in ds:
                p, q = i + d0, j + d1
                if p == -1 or p == n or q == -1 or q == n or grid[p][q] == 0 or grid[p][q] == -1:
                    continue
                dfs(p, q)

        # get the first 1
        for k in range(n):
            for l in range(n):
                if grid[k][l] == 1:
                    dfs(k, l)
                    break
            else:
                continue
            break
        # then, use BFS to search the first "1" encountered
        # this is guaranteed to be the shortest one (minimum flips)
        d = 0
        while queue:
            new_queue = []
            for a0, a1 in queue:
                for d0, d1 in ds:
                    p, q = a0 + d0, a1 + d1
                    if p == -1 or p == n or q == -1 or q == n or grid[p][q] == -1:
                        continue
                    if grid[p][q] == 1:
                        return d
                    # we can also mark visited as -1
                    grid[p][q] = -1
                    new_queue.append((p, q))
            queue = new_queue
            # one round, increment distance
            d += 1
        # should never reach
        return -1


s = Solution()
print(s.shortestBridge([[0, 1], [1, 0]]))
print(s.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
print(s.shortestBridge(
    [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
