# 817. Linked List Components
# You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

# Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.
# Scott 2022/01/13

from typing import List, Optional

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

    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        """
        Time Complexity: O(n1) 94.70%
        Space Complexity: O(n2) 47.02%
        """
        result = 0
        ns = set(nums)
        prev_in = False

        curr = head
        while curr is not None:
            if curr.val not in ns:
                if prev_in:
                    result += 1
                    prev_in = False
            else:
                prev_in = True
            curr = curr.next

        if prev_in:
            result += 1

        return result


if __name__ == '__main__':
    s = Solution()
    
    head = ListNode.create([0,1,2,3])
    nums = [0,1,3]
    print(s.numComponents(head, nums))

    head = ListNode.create([0,1,2,3,4])
    nums = [0,3,1,4]
    print(s.numComponents(head, nums))

    head = ListNode.create([3,4,5,6,1,2,7,8,9,10,0])
    nums = [3,5,7,1,10]
    print(s.numComponents(head, nums))

    head = ListNode.create([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
    nums = [1,2,3,4,5,6,7,8]
    print(s.numComponents(head, nums))

