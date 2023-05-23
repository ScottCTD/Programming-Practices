import heapq
from typing import List

# 2023-05-23 00:19:06
# I previously thought it as the kth smallest
# then it turns out that it's the kth largest: from largest to smallest, the kth element
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        for _ in range(len(nums) - k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
s = KthLargest(3, [4,5,8,2])
print(s.add(3))
print(s.add(5))
print(s.add(10))
print(s.add(9))
print(s.add(4))
