from typing import List

# observation: select one number and left shift it k times is enough
# we just need to find which number to choose

# 2023-05-13 17:30:29
# original
# contest question
# time O(n^2) space O(1)
# exceed time limit
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        max_ = 0
        for i in range(len(nums)):
            num = nums[i]
            nums[i] = num << k
            s = 0
            for j in nums:
                s |= j
            max_ = max(max_, s)
            nums[i] = num
        return max_


class Solution2:
    def maximumOr(self, nums: List[int], k: int) -> int:
        nbits = 45
        a = [0] * nbits
        for num in nums:
            i = nbits - 1
            while num > 0:
                a[i] += num & 1
                num >>= 1
                i -= 1
        max_ = 0
        # try every number and find the max with operations
        for num in nums:
            t = a.copy()
            i = nbits - 1
            while num > 0:
                t[i - k] += num & 1
                t[i] -= num & 1
                num >>= 1
                i -= 1
            # convert list of bits to integer
            c = 0
            for bit in t:
                bit = 1 if bit > 0 else 0
                c = (c << 1) | bit
            max_ = max(max_, c)
        return max_


s = Solution2()
print(s.maximumOr([12, 9], 1))
print(s.maximumOr([8, 1, 2], 2))
