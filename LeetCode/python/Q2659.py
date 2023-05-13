from typing import List

# 2023-05-13 01:30:50
# original
# failed attempt
# exceed time limit
# trash code
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        s = sorted(nums)
        i = 0
        n = len(nums)
        l = n - 1
        a = 0
        count = 0
        while i < n:
            count += 1
            min_ = s[a]
            if nums[i] == min_:
                i += 1
                a += 1
            else:
                nums.append(nums[i])
                i += 1
                n += 1
                l += 1

        return count


s = Solution()
print(s.countOperationsToEmptyArray([-15, -19, 5]) == 5)
