# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Original
    # 72.00%
    # Time O(n)
    # Space O(n)
    def isSymmetric(self, root: TreeNode) -> bool:
        def func(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            if node1.val == node2.val:
                b1 = func(node1.left, node2.right)
                b2 = func(node1.right, node2.left)
                return b1 and b2
            else:
                return False
        return func(root.left, root.right)


root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(Solution().isSymmetric(root))
