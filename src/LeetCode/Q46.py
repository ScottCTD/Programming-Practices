# 给定一个不含重复数字的数组nums，返回其所有可能的全排列。你可以按任意顺序返回答案。
# 2021/07/29 Scott
class Solution:

    # Original
    # 97.51%
    # Backtrack
    def permute(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        result = []
        def backtrack(path: list[int], exist: list[bool]):
            if len(path) == length:
                result.append(path)
                return
            for i in range(length):
                if not exist[i]:
                    exist[i] = True
                    backtrack(path + [nums[i]], exist)
                    exist[i] = False
        backtrack([], [False] * length)
        return result
    
    # Not origianl
    # 100%
    def permute2(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        answer = []
        if n == 1:
            return [nums]
        else:
            result = self.permute2(nums[1:])
            for each in result:
                i = 0
                while i <= n-1:
                    res = each[0:i] + [nums[0]] + each[i:n]
                    answer.append(res)
                    i += 1
        return answer

if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
    print(Solution().permute([0, 1]))
    print(Solution().permute([1]))
    print(Solution().permute2([1, 2, 3]))
    print(Solution().permute2([0, 1]))
    print(Solution().permute2([1]))
