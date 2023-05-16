# 24. Swap Nodes in Pairs
# Medium
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

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


class Solution:

    # 2023-05-16 13:24:53
    # original
    # O(n)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        head = ListNode(next=head)
        prev = head
        while curr is not None and curr.next is not None:
            next_ = curr.next
            curr.next, next_.next = next_.next, curr
            prev.next = next_
            prev = curr
            curr = curr.next
        return head.next


s = Solution()
print(s.swapPairs(ListNode.create([1, 2, 3, 4])))
print(s.swapPairs(ListNode.create([1, 2, 3, 4, 5, 6, 7, 8])))
print(s.swapPairs(ListNode.create([1, 2, 3, 4, 5])))
print(s.swapPairs(ListNode.create([1])))
print(s.swapPairs(None))
