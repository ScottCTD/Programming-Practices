# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

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
    # 88.12%
    # Time O(n)
    # Space O(1)
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
