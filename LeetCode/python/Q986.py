# 986. Interval List Intersections
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]],
                             secondList: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(firstList), len(secondList)
        result = []
        i, j = 0, 0
        # remains are useless, so we finish at the shorter end
        while i < n1 and j < n2:
            l1, l2 = firstList[i], secondList[j]
            # if two intervals are intersected, then we append
            if not (l1[1] < l2[0] or l1[0] > l2[1]):
                result.append([max(l1[0], l2[0]), min(l1[1], l2[1])])
            # if l1 is longer
            if j < n2 - 1 and l1[1] >= l2[1] and l1[1] >= secondList[j + 1][0]:
                j += 1
            # if l2 is longer
            elif i < n1 - 1 and l2[1] >= l1[1] and l2[1] >= firstList[i + 1][0]:
                i += 1
            else:
                i += 1
                j += 1
        return result


s = Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
print(s.intervalIntersection([[1,3],[5,9]], []))
print(s.intervalIntersection([[1,10]], [[2, 4], [5, 6]]))
print(s.intervalIntersection([[14,16]], [[7,13],[16,20]]))

