from typing import List


# 2023-06-03 23:40:28
# original
# TLE
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        matrix = [[-1] * n for _ in range(n)]
        bound = n ** 2
        count = 0
        ans = 0
        row_done = [False] * n
        column_done = [False] * n
        for i in range(len(queries) - 1, -1, -1):
            if count == bound:
                return ans
            type, index, value = queries[i]
            if type == 0 and not row_done[index]:
                row_done[index] = True
                for j in range(n):
                    if matrix[index][j] == -1:
                        matrix[index][j] = value
                        count += 1
                        ans += value
            if type == 1 and not column_done[index]:
                column_done[index] = True
                for j in range(n):
                    if matrix[j][index] == -1:
                        matrix[j][index] = value
                        ans += value
                        count += 1
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
        return ans


# 2023-06-03 23:40:22
# original
class Solution2:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        bound = n ** 2
        count = 0
        ans = 0
        row_done = [False] * n
        column_done = [False] * n
        row_count = 0
        column_count = 0
        for i in range(len(queries) - 1, -1, -1):
            if count == bound:
                return ans
            type, index, value = queries[i]
            if type == 0 and not row_done[index]:
                row_done[index] = True
                row_count += 1
                ans += value * (n - column_count)
                count += (n - column_count)
            if type == 1 and not column_done[index]:
                column_done[index] = True
                column_count += 1
                ans += value * (n - row_count)
                count += (n - row_count)
        return ans



s = Solution2()
print(s.matrixSumQueries(3, [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]))
