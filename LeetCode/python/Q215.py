# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

from typing import List


# 2023-01-19 11:37:28
# original
# time: 1566 ms beats 27.24%
# space: 27.2 MB beats 44.65%
# notes: I implemented the heap, while others used standard library.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_size = len(nums)
        nums = [0] + nums
        # build the heap
        for i in range(heap_size // 2, 0, -1):
            self.heapify(nums, heap_size, i)
        result = 0
        # extract max k times
        for i in range(k):
            result = nums[1]
            nums[1] = nums[heap_size]
            heap_size -= 1
            self.heapify(nums, heap_size, 1)
        return result

    def heapify(self, nums: List[int], heap_size: int, i: int):
        left = i << 1
        right = (i << 1) + 1
        largest = i
        if left <= heap_size and nums[left] > nums[largest]:
            largest = left
        if right <= heap_size and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, heap_size, largest)


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(s.findKthLargest([-1, 2, 0], 3))
