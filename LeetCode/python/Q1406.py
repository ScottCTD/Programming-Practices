# 1406. Stone Game III
# Hard
# Alice and Bob continue their games with piles of stones. There are several stones arranged in
# a row, and each stone has an associated value which is an integer given in the array stoneValue.
#
# Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take
# 1, 2, or 3 stones from the first remaining stones in the row.
#
# The score of each player is the sum of the values of the stones taken. The score of each player
# is 0 initially.
#
# The objective of the game is to end with the highest score, and the winner is the player with the
# highest score and there could be a tie. The game continues until all the stones have been taken.
#
# Assume Alice and Bob play optimally.
#
# Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with
# the same score.

from typing import List


# 2023-05-26 23:23:19
# original
# bottom-up dp
# time 97.96% O(n) space 55.16% O(n)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            s = stoneValue[i]
            dp[i] = s - dp[i + 1]
            if i + 2 <= n:
                s += stoneValue[i + 1]
                dp[i] = max(dp[i], s - dp[i + 2])
                if i + 3 <= n:
                    s += stoneValue[i + 2]
                    dp[i] = max(dp[i], s - dp[i + 3])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'


# 2023-05-26 23:48:56
# inspired
# Solution 1 with space optimization
class Solution2:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp1, dp2, dp3 = 0, 0, 0
        for i in range(n - 1, -1, -1):
            s = stoneValue[i]
            dp0 = s - dp1
            # dp[i] = s - dp[i + 1]
            if i + 2 <= n:
                s += stoneValue[i + 1]
                dp0 = max(dp0, s - dp2)
                if i + 3 <= n:
                    s += stoneValue[i + 2]
                    dp0 = max(dp0, s - dp3)
            dp1, dp2, dp3 = dp0, dp1, dp2
        if dp1 > 0:
            return 'Alice'
        elif dp1 < 0:
            return 'Bob'
        else:
            return 'Tie'


s = Solution2()
print(s.stoneGameIII([1, 2, 3, 7]))
print(s.stoneGameIII([1, 2, 3, -9]))
print(s.stoneGameIII([1, 2, 3, 6]))
