# 113. Path Sum II
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node
# values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:

    # 2022/07/27
    # DFS
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.f(root, targetSum, result, [], 0)
        return result

    def f(self, root: Optional[TreeNode], targetSum: int, paths: List[List[int]], path: List[int], sum_: int):
        if root is None:
            return
        path.append(root.val)
        sum_ += root.val
        if sum_ == targetSum:
            if root.left is None and root.right is None:
                paths.append(path.copy())
                return
        if root.left is not None:
            self.f(root.left, targetSum, paths, path, sum_)
            path.pop()
        if root.right is not None:
            self.f(root.right, targetSum, paths, path, sum_)
            path.pop()


s = Solution()

print(s.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 3))
print(s.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                         TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(11)))), 22))
print(s.pathSum(TreeNode(-2, None, TreeNode(-3)), -5))
