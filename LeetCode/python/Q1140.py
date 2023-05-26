# 1140. Stone Game II
# Medium
# Alice and Bob continue their games with piles of stones.
# There are a number of piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].  The objective of the game is to end with the most stones.
#
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
#
# On each player's turn, that player can take all the stones in the first X remaining piles,
# where 1 <= X <= 2M.  Then, we set M = max(M, X).
#
# The game continues until all the stones have been taken.
#
# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

from typing import List


# 2023-05-26 01:00:50
# learned
# time 52.54 O(n^3) space 61.75% O(n^2)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp[i][m] represent the maximum score that the current player can achieve
        # with piles[i:] and M = m
        # the final answer is dp[0][1]
        n = len(piles)
        # to speed up calculations, we use suffix sum
        suffix_sum = [piles[-1]] * n
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]
        dp = [[0] * (n + 1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                # if we can reach beyond n, then it means that the maximum is just pick all piles
                if i + m * 2 >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    # try all possible X and check the opponent's score
                    for x in range(1, 2 * m + 1):
                        opponent_score = dp[i + x][max(m, x)]
                        # my score is the total score - optimal opponent score
                        score = suffix_sum[i] - opponent_score
                        # use the max one
                        dp[i][m] = max(dp[i][m], score)
        return dp[0][1]


s = Solution()
print(s.stoneGameII([2, 7, 9, 4, 4]))
print(s.stoneGameII([1, 2, 3, 4, 5, 100]))
