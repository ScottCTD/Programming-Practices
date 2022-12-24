# 129. Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated
# so that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.f(root, 0)

    def f(self, root: Optional[TreeNode], prev_total: int) -> int:
        if root is None:
            return 0
        total = prev_total * 10 + root.val
        if root.left is None and root.right is None:
            return total
        return self.f(root.left, total) + self.f(root.right, total)

    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, root.val)])
        result = 0
        while q:
            for _ in range(len(q)):
                node, sum_ = q.popleft()
                if node.left is None and node.right is None:
                    result += sum_
                if node.left is not None:
                    q.append((node.left, sum_ * 10 + node.left.val))
                if node.right is not None:
                    q.append((node.right, sum_ * 10 + node.right.val))
        return result


s = Solution()

print(s.sumNumbers2(TreeNode(1, TreeNode(2), TreeNode(3))))
print(s.sumNumbers2(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))
