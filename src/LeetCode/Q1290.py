# 1290. Convert Binary Number in a Linked List to Integer
# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# Scott 2021/08/22

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
    # 94.67%
    # Time O(n)
    # Space O(n)
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        binary_string = ''
        while node:
            binary_string += str(node.val)
            node = node.next
        return int(binary_string, base=2)