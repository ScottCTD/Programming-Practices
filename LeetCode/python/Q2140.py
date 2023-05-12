# 2140. Solving Questions With Brainpower
# You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
#
# The array describes the questions of an exam, where you have to process the questions in order
# (i.e., starting from question 0) and make a decision whether to solve or skip each question.
# Solving question i will earn you pointsi points but you will be unable to solve each of the next
# brainpoweri questions. If you skip question i, you get to make the decision on the next question.
#
# For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
# If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
# If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will
# be unable to solve questions 2 and 3.
# Return the maximum points you can earn for the exam.

from typing import List


# 2023-05-12 15:01:56
# partially original
# top-down with memoization dp
# time 53.9% space 41.98%
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = [-1] * n

        def f(i: int):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(f(i + 1), questions[i][0] + f(i + questions[i][1] + 1))
            return memo[i]

        return f(0)


# 2023-05-12 15:27:03
# partially original
# bottom-up dp
# time 92.59% space 62.14%
class Solution2:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        # to calculate the max for a "large" one, we need information from smaller pieces
        # smallers are on the right of the array, so we start from the end of the array
        for i in range(n - 1, -1, -1):
            points, skips = questions[i]
            # we need max(solve current, skip)
            dp[i] = max(points + dp[min(n, i + skips + 1)], dp[i + 1])
        return dp[0]



s = Solution2()
print(s.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]))
print(s.mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
