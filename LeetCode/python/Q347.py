# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

from typing import List, Dict
from collections import Counter


# 2023-01-20 01:53:49
# original
# Time: 117 ms beats 55.51%
# Space: 18.4 MB beats 68.59%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap_size = 0
        for i in count:
            # insert i into the heap
            nums[heap_size] = i
            j = heap_size
            heap_size += 1
            parent = (j - 1) >> 1
            while j > 0 and count[nums[j]] < count[nums[parent]]:
                nums[j], nums[parent] = nums[parent], nums[j]
                j = parent
                parent = (j - 1) >> 1
            # if heap_size is k + 1, then we extract the min
            # we need to maintain the size to be k
            if heap_size == k + 1:
                nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
                heap_size -= 1
                self.heapify(count, nums, heap_size, 0)
        # the things left are k-most-frequent
        return nums[:heap_size]

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
