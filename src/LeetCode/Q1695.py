# 1695. Maximum Erasure Value
# You are given an array of positive integers nums and want to erase a subarray containing unique elements.
# The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, 
# that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

class Solution:

    # Original
    # 14.58%
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        result = 0
        left = 0
        right = 1
        length = len(nums)
        if length == 0:
            return 0
        start = 0
        m = {nums[left]: left}
        while left < length:
            while right < length and nums[right] not in m:
                m[nums[right]] = right
                right += 1
            result = max(result, sum(nums[left:right]))
            if right >= length:
                break
            left = m[nums[right]] + 1
            for i in range(start, left):
                m.pop(nums[i])
            start = left
        return result

    # Not Original
    # 100%
    # Same idea as mine but implement way better
    def maximumUniqueSubarray2(self, nums: list[int]) -> int:
        result = temp = nums[0]
        length = len(nums)
        left = 0
        window = {nums[0]}
        for i in range(1, length):
            n = nums[i]
            while n in window:
                l = nums[left]
                window.remove(l)
                temp -= l
                left += 1
            window.add(n)
            temp += n
            result = max(result, temp)
        return result
            

if __name__ == '__main__':
    print(Solution().maximumUniqueSubarray([1]) == 1)
    print(Solution().maximumUniqueSubarray([4,2,4,5,6]) == 17)
    print(Solution().maximumUniqueSubarray([1, 2, 3, 4, 5]) == sum([1, 2, 3, 4, 5]))
    print(Solution().maximumUniqueSubarray([4, 4, 4, 4, 4]) == 4)
    print(Solution().maximumUniqueSubarray([1, 2, 2, 1]) == 3)
    print(Solution().maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]) == 8)
    print(Solution().maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]) == 16911)
    print("Method2===================================================")
    print(Solution().maximumUniqueSubarray2([1]) == 1)
    print(Solution().maximumUniqueSubarray2([4,2,4,5,6]) == 17)
    print(Solution().maximumUniqueSubarray2([1, 2, 3, 4, 5]) == sum([1, 2, 3, 4, 5]))
    print(Solution().maximumUniqueSubarray2([4, 4, 4, 4, 4]) == 4)
    print(Solution().maximumUniqueSubarray2([1, 2, 2, 1]) == 3)
    print(Solution().maximumUniqueSubarray2([5,2,1,2,5,2,1,2,5]) == 8)
    print(Solution().maximumUniqueSubarray2([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]) == 16911)
