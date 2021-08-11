# 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.
# Scott 2021/08/12

# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        head = self
        s = ''
        while head != None:
            s += str(head.val)
            s += ' -> '
            head = head.next
        return s


class Solution:

    # Original
    # 99.32%
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prev = head
        next = head.next
        while next != None:
            if prev.val == next.val:
                prev.next = next.next
            else:
                prev = next
            next = next.next
        return head


if __name__ == '__main__':
    head = ListNode(1, next=ListNode(1, next=ListNode(2)))
    print(Solution().deleteDuplicates(head))
    head = ListNode(1, next=ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(3)))))
    print(Solution().deleteDuplicates(head))