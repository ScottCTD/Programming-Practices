from typing import List

# 2023-05-14 00:52:05
# contest question
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ds = ((-1, 1), (0, 1), (1, 1))
        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j, prev, visited):
            # if (i, j) in visited or i == -1 or i == m or j == n or grid[i][j] <= prev:
            #     return 0
            if dp[i][j] != -1:
                return dp[i][j]
            max_ = 0
            visited.add((i, j))
            for d in ds:
                p = i + d[0]
                q = j + d[1]
                if (p, q) in visited or p == -1 or p == m or q == n or grid[p][q] <= grid[i][j]:
                    continue
                max_ = max(max_, dfs(p, q, grid[i][j], visited))
            visited.remove((i, j))
            dp[i][j] = max_ + 1
            return max_ + 1

        return max(dfs(i, 0, 0, set()) for i in range(m)) - 1


s = Solution()
print(s.maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
print(s.maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]))
print(s.maxMoves([[102, 168, 168, 86, 228],
                  [209, 210, 182, 153, 55],
                  [99, 76, 168, 40, 262],
                  [260, 257, 227, 97, 153],
                  [189, 280, 257, 239, 93],
                  [300, 108, 68, 220, 76]]))
