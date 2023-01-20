# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

from typing import List, Dict


# 2023-01-20 01:53:49
# original
# Time: 117 ms beats 55.51%
# Space: 18.4 MB beats 68.59%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        heap = [0] * (len(count) + 1)
        heap_size = 0
        for i in count:
            # insert i into the heap
            heap[heap_size] = i
            heap_size += 1
            j = heap_size - 1
            parent = (j - 1) >> 1
            while j > 0 and count[heap[j]] < count[heap[parent]]:
                heap[j], heap[parent] = heap[parent], heap[j]
                j = parent
                parent = (j - 1) >> 1
            # if heap_size is k, then we extract the min
            if heap_size == k + 1:
                heap[0], heap[heap_size - 1] = heap[heap_size - 1], heap[0]
                heap_size -= 1
                self.heapify(count, heap, heap_size, 0)
        # the things left are k most frequent
        return heap[:heap_size]

    def heapify(self, count: Dict, heap: List[int], heap_size: int, i: int):
        smallest = i
        left = ((i + 1) << 1) - 1
        right = (i + 1) << 1
        if left < heap_size and count[heap[left]] < count[heap[smallest]]:
            smallest = left
        if right < heap_size and count[heap[right]] < count[heap[smallest]]:
            smallest = right
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify(count, heap, heap_size, smallest)


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))
print(s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
