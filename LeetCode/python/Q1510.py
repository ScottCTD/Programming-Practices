# 1510. Stone Game IV
# Hard
# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there are n stones in a pile. On each player's turn, that player makes a move
# consisting of removing any non-zero square number of stones in the pile.
#
# Also, if a player cannot make a move, he/she loses the game.
#
# Given a positive integer n, return true if and only if Alice wins the game otherwise return false,
# assuming both players play optimally.

class Solution:

    # 2023-05-27 02:36:34
    # original
    # bottom up dp with few optimizations
    # time 50.28% O(n) space 65.92 O(n)
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 2)
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        m = len(squares)
        for i in squares:
            dp[i] = True
            # observation: the one after square must be False
            dp[i + 1] = False
        for i in range(1, n + 1):
            if dp[i]:
                continue
            j = 0
            while j < m and squares[j] <= i:
                if not dp[i - squares[j]]:
                    dp[i] = True
                    break
                j += 1
            else:
                # an observation: if the current is marked with False, then the next one must be T
                dp[i + 1] = True
        return dp[n]


# 2023-05-27 02:48:13
# inspired
# bottom up dp with optimizations
# the key observation is that: If the current one is False, then the next squares must be True.
class Solution2:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 2)
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        m = len(squares)
        for i in squares:
            dp[i] = True
            # observation: the one after square must be False
            dp[i + 1] = False
        for i in range(1, n + 1):
            if dp[i]:
                continue
            for j in squares:
                k = i + j
                if k <= n:
                    # observation: if current is F, then + a square must be T
                    dp[k] = True
                else:
                    break
        return dp[n]

s = Solution()
print(s.winnerSquareGame(1) is True)
print(s.winnerSquareGame(2) is False)
print(s.winnerSquareGame(3) is True)
print(s.winnerSquareGame(4) is True)
print(s.winnerSquareGame(5) is False)
print(s.winnerSquareGame(6) is True)
print(s.winnerSquareGame(7) is False)
print(s.winnerSquareGame(8) is True)
