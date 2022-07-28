# 112. Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a
# root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 2022/07/28
    # BFS
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        q = deque([(root, root.val)])
        while q:
            for _ in range(len(q)):
                node, sum_ = q.popleft()
                if node.left is None and node.right is None:
                    if sum_ == targetSum:
                        return True
                if node.left is not None:
                    q.append((node.left, sum_ + node.left.val))
                if node.right is not None:
                    q.append((node.right, sum_ + node.right.val))
        return False
