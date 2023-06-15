# 1161. Maximum Level Sum of a Binary Tree
# Medium
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and
# so on.
#
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_ = -100001
        ans = 1
        d = 0
        q = [root]
        while q:
            s = 0
            new_q = []
            for node in q:
                s += node.val
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            d += 1
            if s > sum_:
                sum_ = s
                ans = d
            q = new_q
        return ans


s = Solution()
