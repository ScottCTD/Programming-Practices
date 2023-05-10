# 59. Spiral Matrix II
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n2 in spiral order.

from typing import List


class Solution:

    # 2023-05-10 12:27:52
    # original
    # time: O(n^2)
    # space: O(n^2)
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        c = 1
        result = [[0] * n for _ in range(n)]
        while l < r:
            for i in range(l, r):
                result[t][i] = c
                c += 1
            for i in range(t, b):
                result[i][r] = c
                c += 1
            for i in range(r, l, -1):
                result[b][i] = c
                c += 1
            for i in range(b, t, -1):
                result[i][t] = c
                c += 1
            l += 1
            r -= 1
            t += 1
            b -= 1
        if n % 2 != 0:
            result[n // 2][n // 2] = c
        return result


s = Solution()
print(s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
print(s.generateMatrix(1) == [[1]])
print(s.generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
