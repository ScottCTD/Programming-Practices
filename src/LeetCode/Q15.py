# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Scott 2021/07/30
class Solution:

    # Original
    # Relatively Efficient 60.53%
    # Double index with sorted list
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        result = []
        for index in range(length):
            if index and nums[index] == nums[index - 1]:
                continue
            i = index + 1
            j = length - 1
            while i < j:
                sum = nums[index] + nums[i] + nums[j]
                if sum == 0:
                    result.append([nums[index], nums[i], nums[j]])
                    # Move both left and right pointers
                    i += 1
                    # If current value is still equal to the previous one, continue increasing
                    while (i < j and nums[i] == nums[i - 1]):
                        i += 1
                    j -= 1
                    while (i < j and nums[j] == nums[j + 1]):
                        j -= 1
                elif sum > 0:
                    j -= 1
                elif sum < 0:
                    i += 1
        return result


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]),
          [[-1, -1, 2], [-1, 0, 1]])
    print(Solution().threeSum([]), [])
    print(Solution().threeSum([0]), [])
