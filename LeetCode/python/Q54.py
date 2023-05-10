# Given an m x n matrix, return all elements of the matrix in spiral order.

from typing import List

class Solution:

    # Original
    # 2021/08/03
    # 95.1%
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []

        def f(m: list[list[int]], result: list[int]):
            if len(m) == 0:
                return
            result += m[0]
            if len(m) == 1:
                return
            m.pop(0)
            # Append and delete right side
            if len(m) > 0 and len(m[0]) > 0:
                length = len(m[0])
                for i in range(len(m)):
                    result.append(m[i][length - 1])
                    m[i].pop(length - 1)
            # Append and delete bottom
            m[len(m) - 1].reverse()
            result += m[len(m) - 1]
            m.pop(len(m) - 1)
            # Append and delete the left side
            if len(m) > 0 and len(m[0]) > 0:
                for j in range(len(m) - 1, -1, -1):
                    result.append(m[j][0])
                    m[j].pop(0)
            f(m, result)
        f(matrix, result)
        return result


class Solution2:

    # Original
    # 2023/05/09
    # 20.88%
    # Theta(mn)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        r = []
        i, j = 0, 0
        # offsets
        offset = 0
        d = [0, 1]
        while len(r) != m * n:
            r.append(matrix[i][j])
            # collision: j == n - b and d == [0, 1]
            #            i == m - a and d == [1, 0]
            #            j == b and     d == [-1, 0]
            #            i == a and     d == [0, -1]
            if j == n - offset - 1 and d[1] == 1:
                pass
            elif i == m - offset - 1 and d[0] == 1:
                pass
            elif j == offset and d[1] == -1:
                offset += 1
            elif i == offset and d[0] == -1:
                pass
            else:
                i += d[0]
                j += d[1]
                continue
            # change direction: [0, 1] -> [1, 0],
            #                   [1, 0] -> [0, -1],
            #                   [0, -1] -> [-1, 0],
            #                   [-1, 0] -> [0, 1]
            if d[0] == 0:
                d[0], d[1] = d[1], d[0]
            else:
                d[0], d[1] = d[1], -d[0]
            i += d[0]
            j += d[1]
        return r


if __name__ == '__main__':
    print(Solution2().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
          1, 2, 3, 6, 9, 8, 7, 4, 5])
    print(Solution2().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
          1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    print(Solution2().spiralOrder([[3], [2]]) == [3, 2])
    print(Solution2().spiralOrder([[1]]) == [1])
    print(Solution2().spiralOrder([[1], [2], [3]]) == [1, 2, 3])
    print(Solution2().spiralOrder([[1], [2], [3], [4]]) == [1, 2, 3, 4])
    print(Solution2().spiralOrder([[1], [2], [3], [4], [5]]) == [1, 2, 3, 4, 5])
    print(Solution2().spiralOrder([[]]) == [])
    print(Solution2().spiralOrder([[1, 2]]) == [1, 2])
    print(Solution2().spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3])
