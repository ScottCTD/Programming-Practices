# 445. Add Two Numbers II
# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Scott 2021/08/23

from typing import List


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
    # 82.30%
    # Time O(n)
    # Space O(n)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = l1
        n1 = 0
        while node:
            n1 = n1 * 10 + node.val
            node = node.next
        node = l2
        n2 = 0
        while node:
            n2 = n2 * 10 + node.val
            node = node.next
        n = n1 + n2
        stack = []
        while n:
            stack.append(n % 10)
            n //= 10
        if not stack:
            return ListNode(0)
        head = node = ListNode(stack.pop())
        while stack:
            node.next = ListNode(stack.pop())
            node = node.next
        return head


if __name__ == '__main__':
    print(Solution().addTwoNumbers(ListNode.create([7,2,4,3]), ListNode.create([5,6,4])))
    print(Solution().addTwoNumbers(ListNode.create([0]), ListNode.create([5])))
    print(Solution().addTwoNumbers(ListNode.create([0]), ListNode.create([0])))