# 1232. Check If It Is a Straight Line
# Easy
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the
# coordinate of a point. Check if these points make a straight line in the XY plane.
from typing import List


# 2023-06-04 20:22:43
# original
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        dx = x2 - x1
        if dx == 0:
            for i in range(2, len(coordinates)):
                x, y = coordinates[i]
                if x != x1:
                    return False
        else:
            w = (y2 - y1) / (x2 - x1)
            b = y1 - w * x1
            for i in range(2, len(coordinates)):
                x, y = coordinates[i]
                if y != w * x + b:
                    return False
        return True


s = Solution()
print(s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(s.checkStraightLine([[0, 0], [0, 1], [0, -1]]))
print(s.checkStraightLine([[1, 2], [2, 3], [3, 5]]))
print(s.checkStraightLine([[0, 0], [0, 1], [0, -1]]))
print(s.checkStraightLine([[2, 4], [2, 5], [2, 8]]))
