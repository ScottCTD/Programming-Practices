# 1146. Snapshot Array
# Medium
# 2.2K
# 315
# Companies
# Implement a SnapshotArray that supports the following interface:
#
# SnapshotArray(int length) initializes an array-like data structure with the given length.
# Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we
# called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot
# with the given snap_id


# 2023-06-10 20:44:45
# learned
# binary search
class SnapshotArray:

    def __init__(self, length: int):
        #           snap, val
        self.array = [[[0, 0]] for _ in range(length)]
        self.snap_idx = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_idx, val])

    def snap(self) -> int:
        self.snap_idx += 1
        return self.snap_idx - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.array[index]
        if snaps[-1][0] <= snap_id:
            return snaps[-1][1]
        i, j = 0, len(snaps)
        while i < j:
            m = (i + j) // 2
            if snaps[m][0] <= snap_id:
                i = m + 1
            else:
                j = m
        return snaps[i - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

s = SnapshotArray(2)
print(s.set(0, 12))
print(s.snap())
print(s.snap())
print(s.get(1, 0))
print(s.get(1, 0))
print(s.snap())
print(s.snap())
