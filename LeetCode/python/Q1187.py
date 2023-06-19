# 1187. Make Array Strictly Increasing
# Hard
# Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero)
# needed to make arr1 strictly increasing.
#
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do
# the assignment arr1[i] = arr2[j].
#
# If there is no way to make arr1 strictly increasing, return -1.
from typing import List


# 2023-06-19 15:21:49
# learned
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {}
        arr2.sort()

        def dfs(i, prev):
            if i == len(arr1):
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]

            cost = float('inf')

            # If arr1[i] is already greater than prev, we can leave it be.
            if arr1[i] > prev:
                cost = dfs(i + 1, arr1[i])

            # Find a replacement with the smallest value in arr2.
            idx = bisect.bisect_right(arr2, prev)

            # Replace arr1[i], with a cost of 1 operation.
            if idx < len(arr2):
                cost = min(cost, 1 + dfs(i + 1, arr2[idx]))

            dp[(i, prev)] = cost
            return cost

        res = dfs(0, -1)

        return res if res < float('inf') else -1


s = Solution()
