# 551. Student Attendance Record I
# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.
# Scott 2021/08/17

class Solution:

    # Original
    # 94.53%
    # Same idea but use python builtin C functions
    def checkRecord2(self, s: str) -> bool:
        return not (s.count('A') >= 2 or s.find('LLL') != -1)

    # Original
    # 45.99%
    # Time O(n)
    # Space O(1)
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for i in range(len(s)):
            c = s[i]
            if c == 'A':
                absent += 1
                late = 0
            elif c == 'L':
                late += 1
            else:
                late = 0
            if absent >= 2:
                return False
            if late >= 3:
                return False
        return True