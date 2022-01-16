# 25. Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

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
    # 2022/01/16 Scott
    # Original
    # Time Complexity: O(n) 80.91%
    # Space Complexity: O(1) 37.81%
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr is not None:
            curr = curr.next
            n += 1
        group_n = n // k
        h1 = head
        dummy = ListNode(next=h1)
        for i in range(group_n):
            curr = h1
            for _ in range(k - 1):
                curr = curr.next
            h2 = curr.next
            curr.next = None

            prev = None
            node = h1
            while node.next:
                next = node.next
                node.next = prev
                prev = node
                node = next
            node.next = prev

            dummy.next = node
            if i == 0:
                head = dummy.next
            dummy = h1
            h1.next = h2
            h1 = h2
        return head

if __name__ == '__main__':
    s = Solution()

    print(s.reverseKGroup(ListNode.create([1,2,3,4,5]), 2))
    print(s.reverseKGroup(ListNode.create([1,2,3,4,5]), 3))
    print(s.reverseKGroup(ListNode.create([1,2,3,4,5,6,7,8,9,10]), 3))
