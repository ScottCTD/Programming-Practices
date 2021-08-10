# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution:

    # Original
    # 72.54%
    def missingNumber(self, nums: list[int]) -> int:
        a = [-1] * (len(nums) + 1)
        for n in nums:
            a[n] = 0
        for i in range(len(a)):
            if a[i] == -1:
                return i
        return i + 1

    # Not original
    # sum of a list of numbers = n (n + 1) / 2
    def missingNumber2(self, nums: list[int]) -> int:
            n = len(nums)
            return n * (n + 1) // 2 - sum(nums)

if __name__ == '__main__':
    print(Solution().missingNumber([3,0,1]) == 2)
    print(Solution().missingNumber([0,1]) == 2)
    print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8)
    print(Solution().missingNumber([0]) == 1)
    print("===================================")
    print(Solution().missingNumber2([3,0,1]) == 2)
    print(Solution().missingNumber2([0,1]) == 2)
    print(Solution().missingNumber2([9,6,4,2,3,5,7,0,1]) == 8)
    print(Solution().missingNumber2([0]) == 1)