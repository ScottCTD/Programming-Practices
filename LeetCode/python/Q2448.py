# 2448. Minimum Cost to Make Array Equal
# Hard
# You are given two 0-indexed arrays nums and cost consisting each of n positive integers.
#
# You can do the following operation any number of times:
#
# Increase or decrease any element of the array nums by 1.
# The cost of doing one operation on the ith element is cost[i].
#
# Return the minimum total cost such that all the elements of the array nums become equal.
from typing import List


# 2023-06-20 23:25:51
# learned
# try every base
# sort to decrease computation cost (we can calculate the cost change from the previous cost)
# there's also a better way using binary search and convex function, which is very smart.
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        new_nums = sorted(zip(nums, cost), key=lambda e: e[0])
        prefix_sum = [new_nums[0][1]]
        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + new_nums[i][1])
        # calculate the first cost
        prev_num = new_nums[0][0]
        prev_cost = 0
        for i in range(1, n):
            prev_cost += (new_nums[i][0] - prev_num) * new_nums[i][1]
        ans = prev_cost
        # calculate remaining costs based on first cost
        for i in range(1, n):
            gap = new_nums[i][0] - prev_num
            prev_cost += gap * prefix_sum[i - 1]
            #                   total cost     - prefix cost
            prev_cost -= gap * (prefix_sum[-1] - prefix_sum[i - 1])
            prev_num = new_nums[i][0]
            ans = min(ans, prev_cost)

        return ans


s = Solution()
print(s.minCost([1, 3, 5, 2], [2, 3, 1, 14]))
