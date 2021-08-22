# 143. Reorder List
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

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

    # Not really original because I used hints
    # 82.08%
    def reorderList(self, head: ListNode) -> None:
        # Special Case
        if not head.next:
            return head
        # Find the middle of the list
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # Reverse the second half of the list
        prev = None
        node = slow.next
        while node.next:
            next = node.next
            node.next = prev
            prev = node
            node = next
        node.next = prev
        # Insert the reversed second half list into the first half
        first = head
        while first is not slow:
            next1 = first.next
            next2 = node.next

            first.next = node
            first = next1
            
            node.next = next1
            node = next2
        first.next = node

if __name__ == '__main__':
    s = Solution()

    head = ListNode.create([1,2,3,4])
    s.reorderList(head)
    print(head)

    head = ListNode.create([1,2,3,4,5])
    s.reorderList(head)
    print(head)
    
    head = ListNode.create([1])
    s.reorderList(head)
    print(head)