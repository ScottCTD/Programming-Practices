from typing import List


# 2023-06-11 01:07:01
# learned
# lessen learned: sometimes brute force is good
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        min_costs = nums.copy()
        ans = 10 ** 15
        for i in range(n):
            s = 0
            for j in range(n):
                idx = (j + i) % n
                min_costs[j] = min(min_costs[j], nums[idx])
                s += min_costs[j]
            ans = min(ans, s + i * x)
        return ans


s = Solution()
print(s.minCost([20, 1, 15], 5))
