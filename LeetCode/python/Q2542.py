# 2542. Maximum Subsequence Score
# Medium
# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive
# integer k. You must choose a subsequence of indices from nums1 of length k.
#
# For chosen indices i0, i1, ..., ik - 1, your score is defined as:
#
# The sum of the selected elements from nums1 multiplied with the minimum of the selected
# elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1],
# ... ,nums2[ik - 1]).
# Return the maximum possible score.
#
# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1}
# by deleting some or no elements.

from typing import List
import heapq

# 2023-05-24 00:51:19
# learned
# time 96.56% O(nlogn) space 64.89% O(n)
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # firstly sort both arrays based on nums2 in decreasing order
        nums = sorted([(a, b) for a, b in zip(nums1, nums2)], key=lambda e: e[1], reverse=True)
        # we assume that the first k elements are good
        # then, we check each element after k elements to see if that's real good
        # we use a heap to do this efficiently
        heap = [nums[i][0] for i in range(k)]
        heapq.heapify(heap)
        s = sum(heap)
        r = s * nums[k - 1][1]
        for i in range(k, len(nums1)):
            # since we now have fixed an number in num2, we want to take the maximum in nums1
            # we must select nums1[i] because we fixed nums[i], so to find the maximum, we can
            # pop a minimum in current nums1
            num1 = nums[i][0]
            # the reason that we don't do comparison with poped element here is that
            # if the current element is even smaller, then it will be popped in the next round
            # then it won't affect the final answer
            s -= heapq.heapreplace(heap, num1)
            s += num1
            r = max(r, s * nums[i][1])
        return r
