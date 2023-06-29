# 864. Shortest Path to Get All Keys
# Hard
# You are given an m x n grid grid where:
#
# '.' is an empty cell.
# '#' is a wall.
# '@' is the starting point.
# Lowercase letters represent keys.
# Uppercase letters represent locks.
# You start at the starting point and one move consists of walking one space in one of the four
# cardinal directions. You cannot walk outside the grid, or walk into a wall.
#
# If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its
# corresponding key.
#
# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k
# letters of the English alphabet in the grid. This means that there is exactly one key for each
# lock, and one lock for each key; and also that the letters used to represent the keys and locks
# were chosen in the same order as the English alphabet.
#
# Return the lowest number of moves to acquire all keys. If it is impossible, return -1.
from typing import List, Optional
from collections import deque, defaultdict
import heapq
import bisect

# 2023-06-29 00:23:33
# original
# BFS + big manipulation
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        # find start and the complete key set
        key_set = 0
        si, sj = 0, 0
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '.':
                    continue
                if c == '@':
                    si, sj = i, j
                elif (a := ord(c)) >= 97:
                    key_set |= 1 << a % 6

        # perform BFS
        qu = deque()
        #          i , j , s, keys (bit set)
        qu.append((si, sj, 0, 0))
        # if we have visited (i, j) with the same key, then we don't need to visit it again
        visited = set()
        while qu:
            i, j, s, keys = qu.popleft()
            if (i, j, keys) in visited:
                continue
            visited.add((i, j, keys))
            for di, dj in D:
                ni, nj = i + di, j + dj
                if ni == -1 or nj == -1 or ni == m or nj == n or grid[ni][nj] == '#':
                    continue
                c = grid[ni][nj]
                a = ord(c)
                new_key = keys
                # lower letter
                if a >= 97:
                    new_key |= 1 << (a % 6)
                    if new_key == key_set:
                        return s + 1
                elif a >= 65:
                    # lower the character
                    a += 32
                    # check if in keys
                    if not keys & (1 << a % 6):
                        continue
                qu.append((ni, nj, s + 1, new_key))
        return -1



s = Solution()
print(s.shortestPathAllKeys(["@.a..","###.#","b.A.B"]))  # 8
print(s.shortestPathAllKeys(["@..aA","..B#.","....b"]))  # 6
print(s.shortestPathAllKeys(["@Aa"]))  # -1
print(s.shortestPathAllKeys(["@abcdeABCDEFf"]))  # -1
