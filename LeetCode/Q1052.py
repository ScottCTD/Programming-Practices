# 1052. Grumpy Bookstore Owner
# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store.
# You are given an integer array customers of length n where customers[i] is the number of the customer that enters the
# store at the start of the ith minute and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy.
# You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.
# Scott 2021/08/14

from typing import List


class Solution:

    # Not Original
    # 92.14%
    # Ingenious method
    # Abstract the problem into find max sum of certain number of integers in an array
    def maxSatisfied2(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        result = 0
        for i in range(n):
            if not grumpy[i]:
                result += customers[i]
                customers[i] = 0
        window_start = 0
        extra = 0
        temp = 0
        for i in range(n):
            temp += customers[i]
            if i - window_start + 1 > minutes:
                temp -= customers[window_start]
                window_start += 1
            if temp > extra:
                extra = temp
        return result + extra

    # Half Original
    # 5.03%
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        result = 0
        for i in range(n):
            if not grumpy[i]:
                result += customers[i]
                customers[i] = 0
        extra = 0
        for i in range(n - minutes + 1):
            temp = 0
            for j in range(minutes):
                temp += customers[i + j]
            extra = max(extra, temp)
        return result + extra


if __name__ == '__main__':
    print(Solution().maxSatisfied2(
        [1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16)
    print(Solution().maxSatisfied2([1], [0], 1) == 1)
