# 32. Longest Valid Parentheses
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
# Scott 2021/08/23 Failed

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        longest = 0

        return longest


if __name__ == '__main__':
    print(Solution().longestValidParentheses("(()"))
    print(Solution().longestValidParentheses(")()())"))
    print(Solution().longestValidParentheses(""))
    print(Solution().longestValidParentheses("(())("))
    print(Solution().longestValidParentheses("((()()()))"))
    print(Solution().longestValidParentheses("())(())()()"))
    print(Solution().longestValidParentheses("()()()()(((())((()()((()))))"))
    print(Solution().longestValidParentheses("()()()))())((())()()()()))()))(()()(())("))
