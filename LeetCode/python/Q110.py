# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def __repr__(self):
        return str(self.val)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.f(root) != -1

    def f(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left, right = self.f(root.left), self.f(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1


s = Solution()

print(s.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
