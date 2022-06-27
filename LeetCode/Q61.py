# 61. Rotate List
# Given the head of a linked list, rotate the list to the right by k places.
# Scott 2021/08/20


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

    # Original
    # 91.11%
    # Same method as 100%
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Get the size of the linked list
        if not head:
            return None
        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        if size == 1:
            return head
        node = head
        n = size - k % size
        if n == size:
            return head
        for i in range(n - 1):
            node = node.next
        new_head = node.next
        node.next = None
        node = new_head
        while node.next:
            node = node.next
        node.next = head
        return new_head


if __name__ == '__main__':
    head = ListNode.create([1, 2, 3, 4, 5])
    print(Solution().rotateRight(head, 2))
    head = ListNode.create([0, 1, 2])
    print(Solution().rotateRight(head, 4))
    head = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(Solution().rotateRight(head, 100))
