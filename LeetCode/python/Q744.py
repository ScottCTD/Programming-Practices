# 744. Find Smallest Letter Greater Than Target
# Easy
# 3.1K
# 2K
# Companies
# You are given an array of characters letters that is sorted in non-decreasing order, and a
# character target. There are at least two different characters in letters.
#
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.
from typing import List


# 2023-06-09 01:56:28
# original
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # use binary search for letters[i:j]
        n = len(letters)
        i = 0
        j = n
        s = 0
        while i < j:
            m = (i + j) // 2
            if letters[m] > target:
                j = m
                s = m
            elif letters[m] == target:
                i = m + 1
            else:
                i = m + 1
        return letters[s]


s = Solution()
print(s.nextGreatestLetter(["c", "f", "j"], "a"))
print(s.nextGreatestLetter(["c", "f", "j"], "c"))
print(s.nextGreatestLetter(["a", "b", "c", "d", "e"], "c"))
print(s.nextGreatestLetter(["x", "x", "y", "y"], "z"))
