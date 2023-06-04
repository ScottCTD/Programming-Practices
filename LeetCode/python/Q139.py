# 139. Word Break
# Medium
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
# space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
from typing import List


# 2023-06-03 11:12:03
# original
# dp
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for word in wordDict:
                m = len(word)
                if m <= i and dp[i - m]:
                    dp[i] = s[i - m:i] == word
                if dp[i]:
                    break
        return dp[-1]


s = Solution()
print(s.wordBreak('leetcode', ["leet", "code"]))
print(s.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))
