# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise,
# you have to subtract 1 from it.

class Solution:

    # 2021/08/03
    # Original
    # 99.4%
    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            result += 1
        return result


if __name__ == "__main__":
    print(Solution().numberOfSteps(14) == 6)
    print(Solution().numberOfSteps(8) == 4)
    print(Solution().numberOfSteps(123) == 12)
