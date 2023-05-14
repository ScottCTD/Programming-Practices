# 2466. Count Ways To Build Good Strings
# Given the integers zero, one, low, and high, we can construct a string by starting with an empty
# string, and then at each step perform either of the following:
#
# Append the character '0' zero times.
# Append the character '1' one times.
# This can be performed any number of times.
#
# A good string is a string constructed by the above process having a length between low and high
# \(inclusive).
#
# Return the number of different good strings that can be constructed satisfying these properties.
# Since the answer can be large, return it modulo 109 + 7.

# 2023-05-13 21:02:29
# top down dp
# this way doesn't work, too slow
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        max_zero, max_one = high // zero + 2, high // one + 2
        memo = [[-1] * (max_one) for _ in range(max_zero)]
        def dp(z, o):
            if memo[z][o] != -1:
                return memo[z][o]
            l = z * zero + o * one
            if l > high:
                return 0
            if l < low:
                memo[z][o] = dp(z + 1, o) + dp(z, o + 1)
            else:
                memo[z][o] = 1 + dp(z + 1, o) + dp(z, o + 1)
            return memo[z][o]

        return dp(0, 0) % (10 ** 9 + 7)


# 2023-05-13 22:02:18
# correct but still slow
# dp bottome up
# memo keeps track of the # of good strings that can be formed by row zeros and column ones
class Solution2:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        max_zero, max_one = high // zero + 1, high // one + 1
        memo = [[0] * (max_one) for _ in range(max_zero)]
        for i in range(1, max_zero):
            l = i * zero
            if low <= l <= high:
                memo[i][0] = 1 + memo[i - 1][0]
            else:
                memo[i][0] = memo[i - 1][0]
        for i in range(1, max_one):
            l = i * one
            if low <= l <= high:
                memo[0][i] = 1 + memo[0][i - 1]
            else:
                memo[0][i] = memo[0][i - 1]
        for i in range(1, max_zero):
            for j in range(1, max_one):
                l = i * zero + j * one
                if low <= l <= high:
                    memo[i][j] = (1 + memo[i - 1][j] + memo[i][j - 1]) % 1000000007
                else:
                    memo[i][j] = (memo[i - 1][j] + memo[i][j - 1]) % 1000000007
        return memo[-1][-1]


# what about memo keeps track of the # of strings from length 0 to high
# 2023-05-13 22:21:47
# learned
# bottom up dp
# fantastic idea
class Solution3():
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        r = 1000000007
        memo = [0] * (high + 1)
        # there's one string of length 0
        memo[0] = 1
        for i in range(min(zero, one), high + 1):
            if i >= zero:
                memo[i] = (memo[i - zero]) % r
            if i >= one:
                memo[i] = (memo[i] + memo[i - one]) % r
        # count all string between low and high
        res = 0
        for i in range(low, high + 1):
            res = (res + memo[i]) % r
        return res


s = Solution3()
print(s.countGoodStrings(3, 3, 1, 1) == 8)
print(s.countGoodStrings(2, 3, 1, 2) == 5)
print(s.countGoodStrings(1000, 1000, 6, 9) == 0)
print(s.countGoodStrings(45360, 45360, 10, 2) == 398974296)
