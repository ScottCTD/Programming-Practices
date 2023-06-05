# 740. Delete and Earn
# Medium
# You are given an integer array nums. You want to maximize the number of points you get by
# performing the following operation any number of times:
#
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element
# equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of
# times.
from typing import List


# 2023-06-05 17:15:27
# original
# dp (could do space optimization)
# comparable with the best solution
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = sorted(nums)
        new_nums = [[nums[0], 0]]
        for num in nums:
            if new_nums[-1][0] == num:
                new_nums[-1][1] += 1
            else:
                new_nums.append([num, 1])
        n = len(new_nums)
        dp = [0] * (n + 1)
        dp[1] = new_nums[0][0] * new_nums[0][1]
        for i in range(2, n + 1):
            num, count = new_nums[i - 1]
            if num - 1 == new_nums[i - 2][0]:
                dp[i] = max(dp[i - 1], dp[i - 2] + num * count)
            else:
                dp[i] = dp[i - 1] + num * count
        return dp[-1]


s = Solution()
print(s.deleteAndEarn([3, 4, 2]))
print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))
