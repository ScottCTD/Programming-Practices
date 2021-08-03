class Solution:

    # Not Original
    # 2021/08/03
    # 97.63%
    # First sort the interval based on the start of the interval
    # Then if an interval's start is greater than the last merged interval's end,
    # append it to the merged intervals.
    # Else, update the last merged interval's end to the max of the original and the new one.
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result
            

if __name__ == '__main__':
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]])
    print(Solution().merge([[1,4],[4,5]]) == [[1,5]])