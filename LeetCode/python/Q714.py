# 714. Best Time to Buy and Sell Stock with Transaction Fee
# Medium
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and
# an integer fee representing a transaction fee.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but
# you need to pay the transaction fee for each transaction.
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock
# before you buy again).
from typing import List


# 2023-06-22 00:54:28
# original + learned a bit
# dp
# there's a greedy solution but I practice dp now, and I'm tiered.
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # two states for each day: hold or free
        dp = [[0, 0]] * n
        dp[0][0] = -prices[0]
        for i in range(1, n):
            # hold:    max(buy the new one,          do nothing)
            dp[i][0] = max(dp[i - 1][1] - prices[i], dp[i - 1][0])
            # free:    max(sell,                           do nothing)
            dp[i][1] = max(dp[i - 1][0] + prices[i] - fee, dp[i - 1][1])
        # we must free our stock to get the maximum score
        return dp[-1][1]


s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))
