# 1575. Count All Possible Routes
# You are given an array of distinct positive integers locations where locations[i] represents the
# position of city i. You are also given integers start, finish and fuel representing the starting
# city, ending city, and the initial amount of fuel you have, respectively.
#
# At each step, if you are at city i, you can pick any city j such that j != i and
# 0 <= j < locations.length and move to city j. Moving from city i to city j reduces the amount of
# fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value
# of x.
#
# Notice that fuel cannot become negative at any point in time, and that you are allowed to visit
# any city more than once (including start and finish).
#
# Return the count of all possible routes from start to finish. Since the answer may be too large,
# return it modulo 10**9 + 7.
from typing import List


# 2023-06-24 22:51:38
# original
# memoization
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 10 ** 9 + 7
        # memo[(i, rf)] = ans
        memo = {}

        def f(i, rf):
            if (i, rf) in memo:
                return memo[(i, rf)]
            r = 0
            for j in range(n):
                if j == i:
                    continue
                new_rf = rf - abs(locations[j] - locations[i])
                if new_rf < 0:
                    continue
                if j == finish:
                    r += 1
                r += f(j, new_rf)
                r %= MOD
            memo[(i, rf)] = r
            return r

        ans = f(start, fuel) + int(start == finish)
        # print(memo)
        return ans


s = Solution()
print(s.countRoutes([2, 3, 6, 8, 4], 1, 3, 5))
print(s.countRoutes([4, 3, 1], 1, 0, 6))
print(s.countRoutes([5, 2, 1], 0, 2, 3))
print(s.countRoutes([2, 1, 5], 0, 0, 3))
