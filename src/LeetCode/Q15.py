# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        length = len(nums)
        result = []
        for i in range(length):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, length):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        return result

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
    print(Solution().threeSum([]), [])
    print(Solution().threeSum([0]), [])