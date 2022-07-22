# 82. Remove Duplicates from Sorted List II
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list. Return the linked list sorted as well.
# Scott 2021/08/20

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
    # 96.35%
    # Same method as 100%
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(next=head)
        prev = dummy
        node = dummy.next
        while node and node.next:
            if node.val == node.next.val:
                node = node.next
                while node.next and node.val == node.next.val:
                    node = node.next
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return dummy.next


if __name__ == '__main__':
    print(Solution().deleteDuplicates(ListNode.create([1, 2, 3, 3, 4, 4, 5])))
    print(Solution().deleteDuplicates(ListNode.create([1, 1, 1, 2, 3])))
    print(Solution().deleteDuplicates(
        ListNode.create([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])))
