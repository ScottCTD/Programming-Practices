# 496. Next Greater Element I
# The next greater element of some element x in an array is the first greater element 
# that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
# and determine the next greater element of nums2[j] in nums2. 
# If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
# Scott 2021/08/23

from typing import List

class Solution:

    # Original Brute force
    # 28%
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            a = nums1[i]
            if a in nums2:
                found = False
                index = nums2.index(a)
                for j in range(index + 1, len(nums2)):
                    b = nums2[j]
                    if b > a:
                        found = True
                        result.append(b)
                        break
                if not found:
                    result.append(-1)
            else:
                result.append(-1)
        return result
            