# 86. Partition List
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

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

    def __repr__(self) -> str:
        return str(self)


class Solution:

    # 2022/01/18 Scott 30 Minutes
    # Time Complexity: O(n) 99.17%
    # Space Complexity: O(1) 10.11%
    def partition(self, head: ListNode, x: int) -> ListNode:
        result = head
        while result is not None and result.val >= x:
            result = result.next
        if result is None:
            return head

        head2 = ListNode()
        curr2 = head2
        prev = ListNode(next=head)
        curr = head

        while curr.next is not None:
            if curr.val >= x:
                next = curr.next
                curr.next = None
                
                curr2.next = curr
                curr2 = curr

                prev.next = next
                curr = next
            else:
                prev = prev.next
                curr = curr.next

        if curr.val >= x:
            curr2.next = curr
            prev.next = head2.next
        else:
            curr.next = head2.next

        return result

            
if __name__ == '__main__':
    s = Solution()
    
    print(s.partition(ListNode.create([1,4,3,2,5,2]), 3))
    print(s.partition(ListNode.create([2,1]), 2))
    print(s.partition(ListNode.create([9,8,7,6,5,4,3,2,1]), 0))
    print(s.partition(ListNode.create([1,4,2,3,4,5,5,3,4,5,65,7,7,4,34,3,4,5,6,7,7,46,5,5,34,54,65,7,7,8]), 5))
    print(s.partition(ListNode.create([1,5,7,7,8]), 5))