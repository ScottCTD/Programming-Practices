# Given an m x n matrix, return all elements of the matrix in spiral order.

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


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
          1, 2, 3, 6, 9, 8, 7, 4, 5])
    print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
          1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    print(Solution().spiralOrder([[3], [2]]) == [3, 2])
    print(Solution().spiralOrder([[1]]) == [1])
    print(Solution().spiralOrder([[1], [2], [3]]) == [1, 2, 3])
    print(Solution().spiralOrder([[1], [2], [3], [4]]) == [1, 2, 3, 4])
    print(Solution().spiralOrder([[1], [2], [3], [4], [5]]) == [1, 2, 3, 4, 5])
    print(Solution().spiralOrder([[]]) == [])
    print(Solution().spiralOrder([[1, 2]]) == [1, 2])
    print(Solution().spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3])
