# 1721. Swapping Nodes in a Linked List
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Scott 2022/01/10

from typing import Optional


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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        for i in range(k - 1):
            fast = fast.next
        
        first = fast

        slow = head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        first.val, slow.val = slow.val, first.val

        return head


if __name__ == '__main__':
    s = Solution()

    head = ListNode.create([7,9,6,6,7,8,3,0,9,5])
    print(s.swapNodes(head, 5))
