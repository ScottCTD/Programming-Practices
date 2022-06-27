# 147. Insertion Sort List
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

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
    # 95.21%
    # Time O(n^2)
    # Space O(1)
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        prev = head
        node = head.next
        max = head.val
        while node:
            val = node.val
            if val >= max:
                max = val
                node = node.next
                prev = prev.next
            else:
                prev.next = node.next
                temp = dummy.next
                prev2 = dummy
                while temp.val < val:
                    temp = temp.next
                    prev2 = prev2.next
                prev2.next = node
                node.next = temp

                node = prev.next
        return dummy.next


if __name__ == '__main__':
    print(Solution().insertionSortList(ListNode.create([4, 2, 1, 3])))
    print(Solution().insertionSortList(ListNode.create([-1, 5, 3, 4, 0])))
    print(Solution().insertionSortList(ListNode.create([-1])))
