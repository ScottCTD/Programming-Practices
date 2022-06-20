# 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from typing import List


class Solution:

    # WIP
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        n1, n2 = len(s), len(p)
        dct = {c: False for c in p}
        for i in range(0, n1 - n2 + 1):
            for j in range(i, i + n2):
                anagram = True
                c = s[j]
                if c in dct and not dct[c]:
                    dct[c] = True
                else:
                    anagram = False
                    break
            dct = {c: False for c in p}
            if anagram:
                result.append(i)
        return result


s = Solution()
print(s.findAnagrams('baa', 'aa'))