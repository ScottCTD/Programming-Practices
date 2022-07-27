# 116. Populating Next Right Pointers in Each Node
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
from typing import Optional


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        if self.next is None:
            return f'{self.val} -> '
        else:
            return f'{self.val} -> {self.next.val}'


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root
        parent = root
        node = root.left
        first = root.left
        while first is not None:
            while parent is not None:
                node.next = parent.left
                node = parent.left
                node.next = parent.right
                node = node.next
                parent = parent.next
            parent = first
            first = first.left
            node = first
        return root


s = Solution()

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
s.connect(root)
