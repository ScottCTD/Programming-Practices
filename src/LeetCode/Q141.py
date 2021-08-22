# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


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

    # Not original
    # 89.52%
    # Space O(1)
    def hasCycle2(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow is not fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    # Original
    # 89.52%
    # But Space O(n) which is not good
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        node = head
        while node:
            if node in s:
                return True
            s.add(node)
            node = node.next
        return False
