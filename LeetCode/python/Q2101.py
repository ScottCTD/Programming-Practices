# 2101. Detonate the Maximum Bombs
# Medium
# You are given a list of bombs. The range of a bomb is defined as the area where its effect can
# be felt. This area is in the shape of a circle with the center as the location of the bomb.
#
# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri].
# xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri
# denotes the radius of its range.
#
# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs
# that lie in its range. These bombs will further detonate the bombs that lie in their ranges.
#
# Given the list of bombs, return the maximum number of bombs that can be detonated if you are
# allowed to detonate only one bomb.
from collections import defaultdict
from typing import List


# 2023-06-01 20:55:54
# original + a bit debug from solution
# DFS
# time 21.65% space 33.91%
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # construct a graph, two nodes are connected if one could fire the other
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]
                d = (xi - xj) ** 2 + (yi - yj) ** 2
                if d <= ri ** 2:
                    graph[i].append(j)
                if d <= rj ** 2:
                    graph[j].append(i)
        # find the maximum length of path
        ans = 1
        for i in range(n):
            visited = set()
            stack = [i]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                for child in graph[node]:
                    stack.append(child)
            ans = max(ans, len(visited))
        return ans


s = Solution()
print(s.maximumDetonation([[2, 1, 3], [6, 1, 4]]))
print(s.maximumDetonation([[1, 1, 5], [10, 10, 5]]))
print(s.maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
print(s.maximumDetonation([[4, 4, 3], [4, 4, 3]]))
print(s.maximumDetonation([[0, 0, 6], [0, 0, 3], [4, 0, 1]]))
print(s.maximumDetonation(
    [[56, 80, 2], [55, 9, 10], [32, 75, 2], [87, 89, 1], [61, 94, 3], [43, 82, 9], [17, 100, 6],
     [50, 6, 7], [9, 66, 7], [98, 3, 6], [67, 50, 2], [79, 39, 5], [92, 60, 10], [49, 9, 9],
     [42, 32, 10]]))
