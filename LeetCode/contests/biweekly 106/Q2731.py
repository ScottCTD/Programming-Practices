from collections import defaultdict
from typing import List


# 2023-06-10 12:21:30
# learned
# important observation: collisions are ignorable
# also observe on how to calculate the sum of distances
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        # collisions are ignorable
        for i in range(n):
            if s[i] == 'R':
                nums[i] += d
            else:
                nums[i] -= d
        # we want to calculate distances between things
        # we sort the array, so non-decreasing
        # distance = nums[i] - nums[i - 1]
        # we want: (nums[1] - nums[0]) + (nums[2] - nums[1]) + (nums[2] - nums[0]) + ...
        # terms can be reordered ...
        nums = sorted(nums)
        ans = 0
        prefix = 0
        for i in range(n):
            ans += i * nums[i] - prefix
            ans %= MOD
            prefix += nums[i]
        return ans


s = Solution()
print(s.sumDistance([-2, 0, 2], 'RLL', 3))
print(s.sumDistance([1, 0], 'RL', 2))
