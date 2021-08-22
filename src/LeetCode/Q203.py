# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

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
    # 91.37%
    # Time O(n)
    # Space O(1)
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        prev = dummy
        node = head
        while node:
            if node.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
            node = node.next
        return dummy.next


if __name__ == '__main__':
    print(Solution().removeElements(ListNode.create([1,2,6,3,4,5,6]), 6))