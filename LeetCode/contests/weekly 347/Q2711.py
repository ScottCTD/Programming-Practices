from typing import List


# 2023-05-28 01:12:45
# original
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        answer = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                tl, br = set(), set()
                i, j = r - 1, c - 1
                while i >= 0 and j >= 0:
                    tl.add(grid[i][j])
                    i -= 1
                    j -= 1
                i, j = r + 1, c + 1
                while i < m and j < n:
                    br.add(grid[i][j])
                    i += 1
                    j += 1
                answer[r][c] = abs(len(tl) - len(br))
        return answer


s = Solution()
print(s.differenceOfDistinctValues([[1, 2, 3], [3, 1, 5], [3, 2, 1]]))
