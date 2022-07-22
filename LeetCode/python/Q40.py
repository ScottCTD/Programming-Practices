# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# 注意：解集不能包含重复的组合。 
# 2021/07/22
# Scott
# 40 ms: Exceed 93%
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        length = len(candidates)
        candidates.sort()

        def backtract(result: list[list[int]], path: list[int], sum: int, start: int):
            if sum > target:
                return
            if sum == target:
                result.append(path)
                return
            for i in range(start, length):
                # 剪枝
                if sum + candidates[i] > target:
                    break
                # 去重
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtract(result, path + [candidates[i]],
                          sum + candidates[i], i + 1)
        result = []
        backtract(result, [], 0, 0)
        return result


if __name__ == "__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
