# 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，
# 找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。
# candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
# 对于给定的输入，保证和为 target 的唯一组合数少于 150 个。
# 2021/07/22 Scott
# 40ms: Exceed 99%
class Solution:

    # 回溯
    # https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
    # 回溯模板：https://mp.weixin.qq.com/s/gjSgJbNbd1eAA5WkA-HeWw
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(candidates: list[int], length: int, begin: int, path: list[int], result: list[list[int]], target):
            if target < 0:
                return
            if target == 0:
                result.append(path)
                return
            for i in range(begin, length):
                dfs(candidates, length, i, path +
                    [candidates[i]], result, target - candidates[i])

        length = len(candidates)
        path = []
        result = []
        dfs(candidates, length, 0, path, result, target)
        return result

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(candidates: list[int], target: int, length: int, sum: int, path: list[int], result: list[list[int]], start: int):
            if sum > target:
                return
            if sum == target:
                result.append(path)
                return
            for i in range(start, length):
                # 剪枝
                if sum + candidates[i] > target:
                    return
                backtrack(candidates, target, length, sum +
                          candidates[i], path + [candidates[i]], result, i)
        candidates.sort()
        result = []
        backtrack(candidates, target, len(candidates), 0, [], result, 0)
        return result


if __name__ == "__main__":
    print(Solution().combinationSum2([2, 3, 6, 7], 7))
    print(Solution().combinationSum2([2, 3, 5], 8))
    print(Solution().combinationSum2([2], 1))
    print(Solution().combinationSum2([1], 1))
    print(Solution().combinationSum2([1], 2))
    print(Solution().combinationSum2([2, 7, 6, 3, 5, 1], 9))
