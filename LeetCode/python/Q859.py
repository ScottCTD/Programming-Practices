# 859. Buddy Strings
# Easy
# Given two strings s and goal, return true if you can swap two letters in s so the result is
# equal to goal, otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and
# swapping the characters at s[i] and s[j].
#
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
from collections import defaultdict


# 2023-07-03 00:50:00
# original
# very efficient
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False
        i1, i2 = -1, -1
        c1 = defaultdict(int)
        r = False
        for i in range(n):
            c = s[i]
            c1[c] += 1
            if c1[c] >= 2:
                r = True
            if c != goal[i]:
                if i1 == -1:
                    i1 = i
                elif i2 == -1:
                    i2 = i
                else:
                    return False
        if i1 == -1 and i2 == -1:
            return r
        if i1 == -1 or i2 == -1:
            return False
        return s[i1] == goal[i2] and s[i2] == goal[i1]


s = Solution()
