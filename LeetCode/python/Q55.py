from typing import List


class Solution:

    # 2022/07/24
    # not original
    # 贪心算法
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_distance = nums[0]
        for i in range(1, n):
            if max_distance < i:
                return False
            max_distance = max(max_distance, i + nums[i])
            if max_distance >= n - 1:
                return True
        return True


s = Solution()

print(s.canJump([2, 3, 1, 1, 4]))
