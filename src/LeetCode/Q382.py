# 328. Odd Even Linked List
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
# Scott 2022/01/10

# Definition for singly-linked list.
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

    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        size = 1
        last = head
        while last.next is not None:
            last = last.next
            size += 1

        i = 1
        prev = ListNode(next=head)
        curr = head
        while curr is not None and i <= size:
            
            # If even
            if i % 2 == 0:
                last.next = curr
                last = last.next
                prev.next = curr.next

                curr.next = None
                curr = prev.next
            else:
                prev = prev.next
                curr = curr.next

            i += 1
        
        return head


if __name__ == '__main__':
    s = Solution()

    head = ListNode.create([1,2,3,4,5])
    print(s.oddEvenList(head))

    head = ListNode.create([2,1,3,5,6,4,7])
    print(s.oddEvenList(head))

    head = ListNode.create([1, 2, 3])
    print(s.oddEvenList(head))

    head = ListNode()
    print(s.oddEvenList(None))
