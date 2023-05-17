# 2130. Maximum Twin Sum of a Linked List
# Medium
# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is
# known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
#
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
# These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
#
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create(l: list[int]):
        if len(l) == 0:
            return None
        head = ListNode(l[0])
        node = head
        for i in range(1, len(l)):
            node.next = ListNode(l[i])
            node = node.next
        return head

    def __repr__(self) -> str:
        node = self
        result = ''
        while node:
            result += str(node.val) + '->'
            node = node.next
        return result + 'None'


# 2023-05-17 11:26:10
# original
# very inefficient
# time 5.9% space 5.9%
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy_head = ListNode(next=head)
        def f(node):
            if node is None:
                return 0, dummy_head
            a, node1 = f(node.next)
            node1 = node1.next
            m = max(a, node1.val + node.val)
            return m, node1
        return f(head)[0]


# 2023-05-17 11:52:57
# almost original
# time O(n) 71.56% space O(1) 58.99%
# reverse linked list
class Solution2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        # this is valid because n is even
        while fast is not None:
            slow = slow.next
            fast = fast.next.next
        # now slow is the first element on the second-half
        # reverse the second half
        # why not the first half? - better!
        # but not implemented here
        prev = None
        while slow.next is not None:
            ne = slow.next
            slow.next = prev
            prev = slow
            slow = ne
        slow.next = prev
        # calculate maximum
        m = 0
        while slow is not None:
            m = max(m, head.val + slow.val)
            slow = slow.next
            head = head.next
        return m


s = Solution2()
print(s.pairSum(ListNode.create([5, 4, 2, 1])))
print(s.pairSum(ListNode.create([4, 2, 2, 3])))
print(s.pairSum(ListNode.create([1, 100000])))
