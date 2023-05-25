# 837. New 21 Game
# Medium
# Alice plays the following game, loosely based on the card game "21".
#
# Alice starts with 0 points and draws numbers while she has less than k points.
# During each draw, she gains an integer number of points randomly from the range [1, maxPts],
# where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.
#
# Alice stops drawing numbers when she gets k or more points.
#
# Return the probability that Alice has n or fewer points.
#
# Answers within 10-5 of the actual answer are considered accepted.


# 2023-05-24 22:37:50
# learned
# brute-force dp
# exceed time limit
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # dp[i] is the probability of obtaining exactly i points
        # we only care about up to n points
        dp = [0.0] * (n + 1)
        # the probability obtaining exactly 0 points is always 1 because we start from 0 points
        dp[0] = 1
        # we fill dp in a bottom-up fashion
        for i in range(1, n + 1):
            # for dp[i], we can get to i in many ways: from i - j to i, where j from 1 to maxPts
            # we have probability of 1 / m for picking any j from [1, m]
            # we start from i - j, so i - j needs to be < k in order for the game to proceed
            for j in range(1, maxPts + 1):
                start = i - j
                if start < 0:
                    break
                if start < k:
                    # start from `start` AND pick j (1 / m probability)
                    dp[i] += dp[start] * (1 / maxPts)
        # we return the OR of probabilities that the points <= n, and the game ends (points >= k)
        return sum(dp[k:])


# 2023-05-24 22:58:45
# half-original
# optimized brute-force
# time 31.36% space 29.66%
class Solution2:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1
        # this represents the sum of previous probabilities
        s = 1
        for i in range(1, n + 1):
            dp[i] += s / maxPts
            # if the game need to proceed
            if i < k:
                s += dp[i]
            d = i - maxPts
            # when i > maxPts, then we know that we cannot go from i - maxPts - 1 to i in one step
            # so we reduce that probability
            if d >= 0 and d < k:
                s -= dp[d]
        return sum(dp[k:])
