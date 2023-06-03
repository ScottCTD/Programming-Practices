# 1376. Time Needed to Inform All Employees
# Medium
# A company has n employees with a unique ID for each employee from 0 to n - 1.
# The head of the company is the one with headID.
#
# Each employee has one direct manager given in the manager array where manager[i] is the direct
# manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination
# relationships have a tree structure.
#
# The head of the company wants to inform all the company employees of an urgent piece of news.
# He will inform his direct subordinates, and they will inform their subordinates, and so on until
# all employees know about the urgent news.
#
# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates
# (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
#
# Return the number of minutes needed to inform all the employees about the urgent news.
from collections import deque
from typing import List


# 2023-06-02 20:53:14
# original
# DFS (recursive)
# time 88.6% space 50.78
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        def dfs(i):
            if informTime[i] == 0:
                return 0
            t = 0
            for child in graph[i]:
                t = max(t, dfs(child))
            return t + informTime[i]

        return dfs(headID)


# 2023-06-02 21:16:21
# learned
# BFS: record path time
# time 89.87% space 88.54%
class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        queue = deque([(headID, 0)])
        ans = 0
        while queue:
            e, t = queue.popleft()
            ans = max(ans, t)
            for child in graph[e]:
                queue.append((child, t + informTime[e]))
        return ans


s = Solution2()
print(s.numOfMinutes(1, 0, [-1], [0]))
print(s.numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]))
print(s.numOfMinutes(6, 2, [2, 2, -1, 2, 3, 3], [0, 0, 1, 2, 0, 0]))
print(s.numOfMinutes(15, 0, [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                     [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
print(s.numOfMinutes(11, 4, [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4],
                     [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]))
