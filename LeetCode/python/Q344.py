# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# Scott 2021/08/17

from typing import List


class Solution:

    # Original
    # 91.17%
    # Time O(n)
    # Space O(1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            c = s[i]
            s[i] = s[-(i + 1)]
            s[-(i + 1)] = c


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)
