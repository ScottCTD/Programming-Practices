# 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from typing import List


class Solution:

    # original 
    # exceeds time limit
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        n1, n2 = len(s), len(p)
        dct = {}
        for c in p:
            if c in dct:
                dct[c] += 1
            else:
                dct[c] = 1
        for i in range(0, n1 - n2 + 1):
            dct2 = dct.copy()
            anagram = True
            for j in range(i, i + n2):
                c = s[j]
                if c in dct2:
                    if dct2[c] != 0:
                        dct2[c] -= 1
                    else:
                        anagram = False
                        break
                else:
                    anagram = False
                    break
            if anagram:
                result.append(i)
        return result

    # learned
    # sliding window
    # we need to maintain a window character by character, instead of clear the window every time
    # like self.findAnagram
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        result = []
        n1, n2 = len(s), len(p)
        if n1 < n2:
            return result

        p_map = [0] * 26
        s_map = [0] * 26
        for i in range(n2):
            p_map[ord(p[i]) - 97] += 1
            s_map[ord(s[i]) - 97] += 1
        if s_map == p_map:
            result.append(0)

        for i in range(n1 - n2):
            s_map[ord(s[i]) - 97] -= 1
            s_map[ord(s[i + n2]) - 97] += 1
            if s_map == p_map:
                result.append(i + 1)
        return result

s = Solution()
print(s.findAnagrams('baa', 'aa'))