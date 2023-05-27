from typing import List


# 2023-05-27 12:06:01
# original
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        results = [[] for _ in range(n)]
        results[0] = [nums[0]]
        for i in range(1, n):
            results[i].extend(results[i - 1])
            results[i].append(nums[i])
            for r in results[i - 1]:
                results[i].append(nums[i] * r)
        return max(results[-1])


s = Solution()
print(s.maxStrength([3, -1, -5, 2, 5, -9]))
