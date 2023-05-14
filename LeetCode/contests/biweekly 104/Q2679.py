from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = 0
        m, n = len(nums), len(nums[0])
        for i in range(m):
            nums[i] = sorted(nums[i])
        j = n - 1
        for i in range(n):
            score += max(nums[k][j] for k in range(m))
            j -= 1
        return score
