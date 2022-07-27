# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 2022/07/27
    # bad question
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.f(root, -2 ** 31 - 1, 2 ** 31)

    def f(self, root: Optional[TreeNode], min_: int, max_: int):
        if root is None:
            return True
        if root.val <= min_ or root.val >= max_:
            return False
        return self.f(root.left, min_, root.val) and self.f(root.right, root.val, max_)


s = Solution()

print(s.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))
print(s.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))))
