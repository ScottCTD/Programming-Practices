# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Original
    # 86.71%
    # Time O(n) Space O(n)
    def isPalindrome(self, head: ListNode) -> bool:
        size = 0
        node = head
        # Find the middle of list
        while node is not None:
            size += 1
            node = node.next
        # Store the first half of the list into an array
        storage = []
        node = head
        for i in range(size // 2):
            storage.append(node.val)
            node = node.next
        if size % 2 != 0:
            node = node.next
        # Iterate the array reversely and check if the list is a palindrome
        for i in range(len(storage) - 1, -1, -1):
            if node.val is not storage[i]:
                return False
            node = node.next
        return True


if __name__ == '__main__':
    node = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(Solution().isPalindrome(node))
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    print(Solution().isPalindrome(node))
    node = ListNode(1, ListNode(2))
    print(Solution().isPalindrome(node))
