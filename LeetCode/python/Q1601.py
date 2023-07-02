# 1601. Maximum Number of Achievable Transfer Requests
# We have n buildings numbered from 0 to n - 1. Each building has a number of employees.
# It's transfer season, and some employees want to change the building they reside in.
#
# You are given an array requests where requests[i] = [fromi, toi] represents an employee's request
# to transfer from building fromi to building toi.
#
# All buildings are full, so a list of requests is achievable only if for each building,
# the net change in employee transfers is zero. This means the number of employees leaving
# is equal to the number of employees moving in. For example if n = 3 and two employees
# are leaving building 0, one is leaving building 1, and one is leaving building 2,
# there should be two employees moving to building 0, one employee moving to building 1,
# and one employee moving to building 2.
#
# Return the maximum number of achievable requests.
from typing import List


# 2023-07-01 21:50:50
# learned
# backtrack
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        buildings = [0] * n
        ans = 0

        def backtrack(i, count) -> None:
            # we have checked all requests
            if i == m:
                if all(b == 0 for b in buildings):
                    nonlocal ans
                    ans = max(ans, count)
                return
            # for each request, we have two options: consider or not consider
            # consider
            f, t = requests[i]
            buildings[f] -= 1
            buildings[t] += 1
            backtrack(i + 1, count + 1)
            buildings[f] += 1
            buildings[t] -= 1
            # not consider
            backtrack(i + 1, count)

        backtrack(0, 0)
        return ans


s = Solution()
print(s.maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))
print(s.maximumRequests(3, [[0, 0], [1, 2], [2, 1]]))
print(s.maximumRequests(4, [[0, 3], [3, 1], [1, 2], [2, 0]]))
