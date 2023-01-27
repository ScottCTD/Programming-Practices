# 621. Task Scheduler
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter
# represents a different task. Tasks could be done in any order. Each task is done in one unit of
# time. For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same
# tasks (the same letter in the array), that is that there must be at least n units of time between
# any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.

from typing import List


# 2023-01-25 00:03:10
# a failed attempt
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        # initialize priorities
        offset = {}
        heap = []
        unique = 0
        for task in tasks:
            if task in offset:
                heap.append([task, offset[task] + n])
                offset[task] += n
            else:
                heap.append([task, unique])
                offset[task] = unique
                unique += 1
        for o in offset:
            offset[o] = 0
        size = len(heap)
        heap_size = size
        # build the min heap
        for i in range(heap_size // 2, -1, -1):
            self.heapify(heap, heap_size, i)
        # extract the elements in a specific way
        result = 0
        while heap_size > 0:
            if heap[0][1] - (result - offset[heap[0][0]]) == 0:
                offset[heap[0][0]] += 1
                heap_size -= 1
                heap[0], heap[heap_size] = heap[heap_size], heap[0]
                self.heapify(heap, heap_size, 0)
            result += 1
        return result

    def heapify(self, heap: List[tuple[str, int]], heap_size: int, i: int):
        smallest = i
        left = (i << 1) + 1
        right = left + 1
        if left < heap_size and heap[left][1] < heap[smallest][1]:
            smallest = left
        if right < heap_size and heap[right][1] < heap[smallest][1]:
            smallest = right
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify(heap, heap_size, smallest)


s = Solution()
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 0))
print(s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
