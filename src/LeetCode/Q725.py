# 725. Split Linked List in Parts
# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

# Return an array of the k parts.

# Scott 2022/01/10

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
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        # Get size
        curr = head
        size = 0
        while curr is not None:
            size += 1
            curr = curr.next

        extra = size % k
        split_size = size // k
        extra_split_size = split_size + 1

        result = []

        curr = head
        while curr is not None:
            if extra > 0:
                result.append(curr)
                for i in range(extra_split_size - 1):
                    curr = curr.next
                extra -= 1
                temp = curr
                curr = curr.next
                temp.next = None
            else:
                result.append(curr)
                for i in range(split_size - 1):
                    curr = curr.next
                extra -= 1
                temp = curr
                curr = curr.next
                temp.next = None

        l = len(result)
        if l < k:
            for i in range(k - l):
                result.append(None)

        return result


if __name__ == '__main__':
    s = Solution()

    head = ListNode.create([1, 2, 3])
    print([str(s) + ' ' for s in s.splitListToParts(head, 5)])

    head = ListNode.create([1,2,3,4,5,6,7,8,9,10])
    print([str(s) + ' ' for s in s.splitListToParts(head, 3)])
