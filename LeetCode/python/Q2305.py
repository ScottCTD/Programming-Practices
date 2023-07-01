# 2305. Fair Distribution of Cookies
# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith
# bag. You are also given an integer k that denotes the number of children to distribute all the
# bags of cookies to. All the cookies in the same bag must go to the same child and cannot be
# split up.
#
# The unfairness of a distribution is defined as the maximum total cookies obtained by a single
# child in the distribution.
#
# Return the minimum unfairness of all distributions.
from typing import List


# 2023-07-01 00:34:50
# learned
# naive backtrack
# TODO: learn more about backtrack
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        # distribute[i] represent the number of cookies for child i
        distribute = [0] * k

        # we want to try every possible distribution
        # returns the minimum unfairness
        def f(i, zeros):
            if n - i < zeros:
                return 10E10
            if i == n:
                return max(distribute)
            ans = 10E10
            for j in range(k):
                zeros -= int(distribute[j] == 0)
                distribute[j] += cookies[i]
                ans = min(ans, f(i + 1, zeros))
                distribute[j] -= cookies[i]
                zeros += int(distribute[j] == 0)
            return ans

        return f(0, k)


s = Solution()
print(s.distributeCookies([8, 15, 10, 20, 8], 2))
print(s.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3))
