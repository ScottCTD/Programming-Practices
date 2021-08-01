# Summary Ranges
# You are given a sorted unique integer array nums.
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, 
# and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
class Solution:

    # Original
    # 94.44%
    def summaryRanges(self, nums: list[int]) -> list[str]:
        length = len(nums)
        if length == 0:
            return []
        elif length == 1:
            return [str(nums[0])]
        result = []
        a = nums[0]
        b = a
        for i in range(0, length):
            b = nums[i]
            if i != length - 1:
                if b + 1 != nums[i + 1]:
                    if a == b:
                        result.append(str(a))
                    else:
                        result.append("{0}->{1}".format(a, b))
                    a = nums[i + 1]
            else:
                if a == b:
                    result.append(str(a))
                else:
                    result.append("{0}->{1}".format(a, b))
        return result

    # Original
    # 98%
    def summaryRanges2(self, nums: list[int]) -> list[str]:
        length = len(nums)
        if length == 0:
            return []
        elif length == 1:
            return [str(nums[0])]
        result = []
        a = 0
        b = a
        for i in range(1, length):
            if nums[i] == nums[b] + 1:
                b = i
            else:
                if a != b:
                    result.append("{0}->{1}".format(nums[a], nums[b]))
                else:
                    result.append(str(nums[a]))
                a = b = i
        if a != b:
            result.append("{0}->{1}".format(nums[a], nums[b]))
        else:
            result.append(str(nums[a]))
        return result

if __name__ == "__main__":
    print(Solution().summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"])
    print(Solution().summaryRanges([1, 2, 3, 4, 5, 6]) == ["1->6"])
    print(Solution().summaryRanges([1, 3]) == ["1", "3"])
    print(Solution().summaryRanges([1, 9, 10, 11, 15]) == ["1", "9->11", "15"])
    print(Solution().summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"])
    print(Solution().summaryRanges([]) == [])
    print(Solution().summaryRanges([-1]) == ["-1"])
    print(Solution().summaryRanges([0]) == ["0"])
    print("Method2")
    print(Solution().summaryRanges2([0,1,2,4,5,7]) == ["0->2","4->5","7"])
    print(Solution().summaryRanges2([1, 2, 3, 4, 5, 6]) == ["1->6"])
    print(Solution().summaryRanges2([1, 3]) == ["1", "3"])
    print(Solution().summaryRanges2([1, 9, 10, 11, 15]) == ["1", "9->11", "15"])
    print(Solution().summaryRanges2([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"])
    print(Solution().summaryRanges2([]) == [])
    print(Solution().summaryRanges2([-1]) == ["-1"])
    print(Solution().summaryRanges2([0]) == ["0"])