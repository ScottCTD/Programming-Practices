# 1222. Queens That Can Attack the King
# On an 8x8 chessboard, there can be multiple Black Queens and one White King.

# Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.

# Scott 2022/01/15

from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """
        Let n = len(queens).
        Time Complexity: O(n) (Not sure) 91.49%
        Space Complexity: O(1) 43.62%
        """
        result = []
        board = [[0 for _ in range(8)] for _ in range(8)]
        for queen in queens:
            board[queen[0]][queen[1]] = 1
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1],
              [1, 1], [-1, -1], [-1, 1], [1, -1]]
        for d in ds:
            x, y = king[0], king[1]
            x += d[0]
            y += d[1]
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 1:
                    result.append([x, y])
                    break
                x += d[0]
                y += d[1]
        return result


if __name__ == '__main__':
    s = Solution()

    print(s.queensAttacktheKing(
        [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], [0, 0]))

    print(s.queensAttacktheKing(
        [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], [3, 3]))

    print(s.queensAttacktheKing([[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2], [1, 1], [6, 4], [
          5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]], [3, 4]))
