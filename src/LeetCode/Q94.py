# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 2022/02/07 Scott
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        if root.left is None:
            return [root.val] + self.inorderTraversal(root.right)
        if root.right is None:
            return self.inorderTraversal(root.left) + [root.val]
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
