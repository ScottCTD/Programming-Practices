# 509. Fibonacci Number
# Easy
# 6.8K
# 315
# Companies
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# 2023-06-05 16:08:15
# original
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp0 = 0
        dp1 = 1
        dp2 = 0
        for i in range(2, n + 1):
            dp2 = dp0 + dp1
            dp0, dp1 = dp1, dp2
        return dp2
