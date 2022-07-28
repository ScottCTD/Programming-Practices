# 111. Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:

    # 2022/07/28
    # DFS
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # 2022/07/28
    # BFS
    def minDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque()
        q.append(root)
        result = 0
        while q:
            n = len(q)
            result += 1
            for _ in range(n):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return result
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return result
