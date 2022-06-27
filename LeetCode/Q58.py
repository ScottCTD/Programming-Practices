# 58. Length of Last Word
# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Scott 2021/08/12

class Solution:

    # Original
    # 82.34%
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        l = len(s)
        for i in range(l - 1, -1, -1):
            if s[i] != ' ':
                result += 1
            elif s[i] == ' ' and result != 0:
                return result
        return result


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World") == 5)
    print(Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4)
    print(Solution().lengthOfLastWord("luffy is still joyboy") == 6)
    print(Solution().lengthOfLastWord(" ") == 0)
