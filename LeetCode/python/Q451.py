# 451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

import heapq
import collections
from typing import List

# 2023-01-24 22:12:03
# original and efficient
# use heapsort to sort the non-duplicate heap
# use counter to add the duplicates back
# Time: 39 ms beats 94.66%
# Space: 15.3 MB beats 39.37%
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = list(counter.keys())
        n = len(heap)
        # build the heap
        for i in range(n // 2, -1, -1):
            # heapify the thing
            self.heapify(heap, n, i, counter)
        # extract min
        while n > 0:
            n -= 1
            # if counter[heap[0]] == counter[heap[n]]:
            #     break
            heap[0], heap[n] = heap[n], heap[0]
            self.heapify(heap, n, 0, counter)
        result = ''
        for c in heap:
            result += c * counter[c]
        return result

    def heapify(self, heap: List[str], heap_size: int, i: int, counter):
        smallest = i
        left = (smallest << 1) + 1
        right = left + 1
        if left < heap_size and counter[heap[left]] < counter[heap[smallest]]:
            smallest = left
        if right < heap_size and counter[heap[right]] < counter[heap[smallest]]:
            smallest = right
        # if smallest == i:
        #     if left < heap_size and heap[left] < heap[smallest]:
        #         smallest = left
        #     if right < heap_size and heap[right] < heap[smallest]:
        #         smallest = right
        if smallest != i:
            heap[smallest], heap[i] = heap[i], heap[smallest]
            self.heapify(heap, heap_size, smallest, counter)


s = Solution()

print(s.frequencySort("tree") == 'eert')
print(s.frequencySort("cccaaa") in {'aaaccc', 'cccaaa'})
print(s.frequencySort("raaeaedere") == "eeeeaaarrd")
print(s.frequencySort("oijsefjiofjoi") == "iiijjjoooffse")
