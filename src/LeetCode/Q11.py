# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        water = 0
        while i < j:
            l, r = height[i], height[j]
            water = max(water, (j - i) * min(l ,r))
            if l > r:
                j -= 1
            else:
                i += 1
        return water