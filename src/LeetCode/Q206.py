# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import overload


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create(l: list[int]):
        head = ListNode(l[0])
        node = head
        for i in range(1, len(l)):
            node.next = ListNode(l[i])
            node = node.next
        return head

    def __str__(self) -> str:
        node = self
        result = ''
        while node:
            result += str(node.val) + '->'
            node = node.next
        return result


class Solution:

    # Same idea as mine but different implementation
    # 96.66%
    def reverseList2(self, head: ListNode) -> ListNode:
        def func(prev, node):
            if node:
                next = node.next
                node.next = prev
                return func(node, next)
            else:
                return prev
        return func(None, head)

    # Original
    # 89.40%
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        node = head
        while node.next:
            next = node.next
            node.next = prev
            prev = node
            node = next
        node.next = prev
        return node


if __name__ == '__main__':
    print(Solution().reverseList2(ListNode.create([1, 2, 3, 4, 5])))
