# 373. Find K Pairs with Smallest Sums
# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u, v) which consists of one element
# from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

from typing import List


# 2023-01-21 00:42:23
# original
# Time: 3402 ms beats 10.80%
# Space: 33 MB beats 75.65%
# bad implementation
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heap_size = 0
        for i in nums1:
            for j in nums2:
                e = [i, j]
                # insert the pair into the heap
                if heap_size < k:
                    if len(heap) <= heap_size:
                        heap.append([0, 0])
                    heap[heap_size] = e
                    a = heap_size
                    heap_size += 1
                    # to the correct position
                    parent = (a - 1) // 2
                    while parent >= 0 and heap[parent][0] + heap[parent][1] < \
                            heap[a][0] + heap[a][1]:
                        heap[parent], heap[a] = heap[a], heap[parent]
                        a = parent
                        parent = (a - 1) // 2
                else:
                    current_max = heap[0]
                    ss = current_max[0] + current_max[1]
                    se = e[0] + e[1]
                    if ss > se:
                        heap[0] = e
                        self.heapify(heap, heap_size, 0)
                    elif ss < se:
                        if j == 0:
                            return heap
                        break
        return heap

    def heapify(self, heap: List[List[int]], heap_size: int, i: int):
        largest = i
        left = (i << 1) + 1
        right = (i << 1) + 2
        if left < heap_size and heap[left][0] + heap[left][1] > heap[largest][0] + heap[largest][1]:
            largest = left
        if right < heap_size and heap[right][0] + heap[right][1] > \
                heap[largest][0] + heap[largest][1]:
            largest = right
        if largest != i:
            heap[largest], heap[i] = heap[i], heap[largest]
            self.heapify(heap, heap_size, largest)


s = Solution()

print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print(s.kSmallestPairs([1, 2], [3], 3))
print(s.kSmallestPairs([0, 0, 2, 2], [-3, 5], 3))
print(s.kSmallestPairs([0, 0, 0, 0, 0, 2, 2, 2, 2], [-3, 22, 35, 56, 76], 22))
print(s.kSmallestPairs([-1, -1, -1, 0, 0, 0, 1, 1], [-1, -1, -1, 0, 0, 0, 1, 1], 10))
