# 218. The Skyline Problem
# refers to https://leetcode.com/problems/the-skyline-problem/description/

from typing import List, Tuple

# 2023-01-27 15:53:22
# original but failed
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        result = [[buildings[0][0], buildings[0][2]]]
        heap = [[buildings[0][1], buildings[0][2]]]
        heap_size = 1
        for building in buildings[1:]:
            p1 = [building[0], building[2]]
            p2 = [building[1], building[2]]
            # if the x of new building is inside the current max building
            if p1[0] <= heap[0][0]:
                # the new building height is greater
                if p1[1] > heap[0][1]:
                    result.append(p1)
                    heap_size = self.insert(heap, heap_size, p2)
                # new building height is smaller
                elif p1[1] < heap[0][1]:
                    # if the right of the new building is greater than the current max
                    if p2[0] > heap[0][0]:
                        result.append([heap[0][0], p2[1]])
                        heap_size = self.insert(heap, heap_size, p2)
                else:
                    pass
            # outside
            elif p1[0] > heap[0][0]:
                maximum, heap_size = self.extract_max(heap, heap_size)
                max_x = maximum[0]
                while heap_size > 0 and heap[0][0] < p1[0]:
                    maximum, heap_size = self.extract_max(heap, heap_size)
                    max_x = max(maximum[0], max_x)
                if heap_size == 0:
                    result.append([max_x, 0])
                    result.append(p1)
                    self.insert(heap, heap_size, p2)
                else:
                    # the new building height is greater
                    if p1[1] > heap[0][1]:
                        result.append(p1)
                        heap_size = self.insert(heap, heap_size, p2)
                    # new building height is smaller
                    elif p1[1] < heap[0][1]:
                        # if the right of the new building is greater than the current max
                        if p2[0] > heap[0][0]:
                            result.append([heap[0][0], p2[1]])
                            heap_size = self.insert(heap, heap_size, p2)
                    else:
                        pass
        result.append([buildings[-1][1], 0])
        return result

    def insert(self, heap: List[List[int]], heap_size: int, x: List[int]) -> int:
        if len(heap) == heap_size:
            heap.append(x)
        else:
            heap[heap_size] = x
        i = heap_size
        heap_size += 1
        while i > 0:
            parent = (i - 1) >> 1
            if heap[parent][1] < heap[i][1]:
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent
            else:
                if heap[parent][1] == heap[i][1]:
                    pass
                break
        return heap_size

    def heapify(self, heap: List[List[int]], heap_size: int, i: int):
        while i > heap_size:
            maximum = i
            left = (i << 1) + 1
            right = left + 1
            if left < heap_size and heap[left][1] > heap[maximum][1]:
                maximum = left
            if right < heap_size and heap[right][1] > heap[maximum][1]:
                maximum = right
            if maximum != i:
                heap[i], heap[maximum] = heap[maximum], heap[i]
                i = maximum
            else:
                break

    def extract_max(self, heap: List[List[int]], heap_size: int) -> \
            Tuple[List[int], int]:
        maximum = heap[0]
        heap_size -= 1
        heap[heap_size], heap[0] = heap[0], heap[heap_size]
        self.heapify(heap, heap_size, 0)
        return maximum, heap_size


s = Solution()
print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]) ==
      [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
print(s.getSkyline([[0, 2, 3], [2, 5, 3]]) == [[0, 3], [5, 0]])
print(s.getSkyline([[0, 2, 3], [1, 4, 3]]) == [[0, 3], [4, 0]])
print(s.getSkyline([[2, 9, 10], [9, 12, 15]]) == [[2, 10], [9, 15], [12, 0]])
print(s.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]) == [[1, 3], [2, 0]])
