# 2657. Find the Prefix Common Array of Two Arrays
# You are given two 0-indexed integer permutations A and B of length n.
#
# A prefix common array of A and B is an array C such that C[i]
# is equal to the count of numbers that are present at or before the index i in both A and B.
#
# Return the prefix common array of A and B.
#
# A sequence of n integers is called a permutation if it contains all integers from 1 to n
# exactly once.

from typing import List

# 2023-05-13 00:18:00
# contest question
# original
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        temp = [0] * n
        res = [0] * n
        for i in range(n):
            temp[A[i] - 1] += 1
            temp[B[i] - 1] += 1
            for j in temp:
                if j == 2:
                    res[i] += 1
        return res