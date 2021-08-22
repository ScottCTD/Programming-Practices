# 92. Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

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
    # 93.79%
    # Time O(n)
    # Space O(1)
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Special case
        if not head.next:
            return head
        # Initialization
        left -= 1
        right -= 1
        dummy = ListNode(next=head)
        node = head
        # Find left bound
        left_bound = None
        start = None
        if left == 0:
            left_bound = dummy
            start = head
        else:
            for j in range(left - 1):
                node = node.next
            left_bound = node
            start = node = node.next
        # Find right bound
        i = left
        while i < right:
            i += 1
            node = node.next
        right_bound = node.next
        # Reverse
        i = left
        prev = right_bound
        while i < right:
            next = start.next
            start.next = prev
            prev = start
            start = next
            i += 1
        start.next = prev
        left_bound.next = start
        return dummy.next


if __name__ == '__main__':
    print(Solution().reverseBetween(ListNode.create([1, 2, 3, 4, 5]), 1, 5))
    print(Solution().reverseBetween(ListNode.create([5, 1, 1]), 2, 3))
    print(Solution().reverseBetween(ListNode.create([1, 2, 3]), 1, 2))
