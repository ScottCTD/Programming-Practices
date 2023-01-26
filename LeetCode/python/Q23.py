# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        node = self
        result = []
        while node is not None:
            result.append(node.val)
            node = node.next
        return str(result)


def create_list_node(l: List[int]):
    head = ListNode(l[0])
    node = head
    for i in range(1, len(l)):
        node.next = ListNode(l[i])
        node = node.next
    return head


# 2023-01-26 18:31:14
# original but not efficient
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        result_head = ListNode()
        # use a heap that keeps k elements
        heap = []
        for i in range(k):
            head = lists[i]
            while head is not None:
                heap.append(head.val)
                head = head.next
        heap_size = len(heap)
        for i in range(heap_size // 2, -1, -1):
            self.heapify(heap, heap_size, i)
        node = result_head
        for _ in range(heap_size):
            heap_size -= 1
            node.next = ListNode(heap[0])
            node = node.next
            heap[0], heap[heap_size] = heap[heap_size], heap[0]
            self.heapify(heap, heap_size, 0)
        return result_head.next

    def heapify(self, heap: List[int], heap_size: int, i: int):
        while i < heap_size:
            smallest = i
            left = (i << 1) + 1
            right = left + 1
            if left < heap_size and heap[left] < heap[smallest]:
                smallest = left
            if right < heap_size and heap[right] < heap[smallest]:
                smallest = right
            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
            else:
                break


# 2023-01-26 18:30:17
# original and efficient
# time complexity: O(nlg(k))
# space complexity: O(n)
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [lst for lst in lists if lst is not None]
        k = len(heap)
        if k == 0:
            return None
        # heapify the whole heap
        for i in range(k // 2, -1, -1):
            self.heapify(heap, k, i)
        result_head = ListNode()
        node = result_head
        while heap[0] is not None:
            # "extract" the min
            node.next = heap[0]
            node = node.next
            heap[0] = heap[0].next
            if heap[0] is None:
                k -= 1
                heap[0], heap[k] = heap[k], heap[0]
            self.heapify(heap, k, 0)
        return result_head.next

    def heapify(self, heap: List[ListNode], heap_size: int, i: int):
        while i < heap_size:
            smallest = i
            left = (i << 1) + 1
            right = left + 1
            if left < heap_size and heap[left].val < heap[smallest].val:
                smallest = left
            if right < heap_size and heap[right].val < heap[smallest].val:
                smallest = right
            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
            else:
                break


s = Solution2()
print(s.mergeKLists(
    [create_list_node([1, 4, 5]), create_list_node([1, 3, 4]), create_list_node([2, 6])]))
print(s.mergeKLists([None, create_list_node([1])]))
