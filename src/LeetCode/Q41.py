# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
# 2021/07/22 Non-original
# 120ms: Exceed 40+% (Someone cheaters not reach O(N))
class Solution:
    # 我们可以发现，数组的下标是0 -> len的
    # 所以如果我们的数组里面有 1 -> len + 1的数的话
    # 我们可以把他们通过交换位置的方式归位：例如2移动到数组第二个格子，也就是下标为1的地方
    # 在交换的过程中可能换过来的数还是在 1 -> len + 1之间的话，我们继续交换直到当前下标所指的数不在正常范围
    # 所以，通过这么多的交换，我们把在范围内的数交换到了正确的位置
    # 例如 [3, 4, -1, 1] -> [1, -1, 3, 4]
    # 可以发现，下标为1的元素不应该处在这个位置上，因为这个位置按理说属于2
    # 所以，又因为现在他是按照顺序排好了，所以这个不正确的位置一定是缺失的数
    # 那如果某个数比数组的容量要大，他去了哪里呢，他一样也在某一个错误的位置上
    # 我们不可能找到一个数字没有中断的并且错误的正整数数组而，因为一旦数组中有错
    # 那么这个数组一定会被中断，例如[1, 2, 3, 4]无错误，[1, 2, 3, 5]有错误（数超过数组大小了）了，但是中断了
    def firstMissingPositive(self, nums: list[int]) -> int:
        length = len(nums)
        for i in range(length):
            while (0 < nums[i] <= length and nums[i] != nums[nums[i] - 1]):
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(length):
            if nums[i] - 1 != i:
                return i + 1
        return length + 1

    def firstMissingPositive2(self, nums: list[int]) -> int:
        length = len(nums)
        exist = [0] * length
        for n in nums:
            if 0 < n <= length:
                exist[n - 1] = 1
        for i in range(length):
            if exist[i] == 0:
                return i + 1
        return length + 1

if __name__ == "__main__":
    print(Solution().firstMissingPositive2([3, 4, -1, 1]))
    print(Solution().firstMissingPositive2([1]))
    print(Solution().firstMissingPositive2([1, 2, 3, 5]))