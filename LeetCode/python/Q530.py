# 530. Minimum Absolute Difference in BST
# Easy
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between
# the values of any two different nodes in the tree.
from typing import List, Optional
from collections import deque, defaultdict
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 2023-06-14 00:15:42
# almost original
# inorder tree traversal
# observation: sort
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev_val = -100001
        self.ans = 100001

        def dfs(root: TreeNode):
            if root.left is not None:
                dfs(root.left)
            self.ans = min(self.ans, root.val - self.prev_val)
            self.prev_val = root.val
            if root.right is not None:
                dfs(root.right)

        dfs(root)

        return self.ans


# 2023-06-14 00:29:42
# original
# iterative inorder tree traversal
class Solution2:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev_val = -100001
        ans = 100001
        stack = [root]
        while stack:
            node = stack[-1]
            if node.left and node.left.val != -1:
                stack.append(node.left)
                continue
            node = stack.pop()
            ans = min(ans, node.val - prev_val)
            prev_val = node.val
            node.val = -1
            if node.right:
                stack.append(node.right)
        return ans


s = Solution2()
print(s.getMinimumDifference(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))))
