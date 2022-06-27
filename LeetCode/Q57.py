# 57. Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.
# Scott 2022/01/14

from typing import List

class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n) 99.55%
        Space Complexity: O(n ) 62.44%
        """
        n = len(intervals)
        result = []
        i = 0

        # Find the position to insert
        while i < n and intervals[i][1] < newInterval[0]:
            i += 1
        result.extend(intervals[:i])

        # Merge the intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        result.append(newInterval)

        result.extend(intervals[i:])

        return result

         
if __name__ == '__main__':
    s = Solution()

    print(s.insert([[1,3],[6,9]], [2,5]))
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
