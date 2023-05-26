from typing import List

# 2023-05-14 00:51:31
# contest question
# failed
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        if derived[0] == 1:
            a = [1, 0]
            for i in range(1, n - 1):
                if derived[i] == 1:
                    a.append(1)
                else:
                    a.append(0)

            if derived[n - 1] == 0 and a[-1] ^ 0 == derived[n - 2]:
                return True
            a = [0, 1]
            for i in range(1, n - 1):
                if derived[i] == 1:
                    a.append(0)
                else:
                    a.append(1)
            if derived[n - 1] == 1 and a[-1] ^ 0 == derived[n - 2]:
                return True
        else:
            a = [0, 0]
            for i in range(1, n - 1):
                if derived[i] == 1:
                    a.append(1)
                else:
                    a.append(0)
            if derived[n - 1] == 0 and a[-1] ^ 0 == derived[n - 2]:
                return True
            a = [1, 1]
            for i in range(1, n - 1):
                if derived[i] == 1:
                    a.append(0)
                else:
                    a.append(1)
            if derived[n - 1] == 1 and a[-1] ^ 0 == derived[n - 2]:
                return True
        return False


class Solution2:

    # 2023-05-16 19:37:57
    # original
    # time O(n) space O(1)
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        if n == 1:
            return not derived[0]
        # observation: don't need to do both [1, 0] and [0, 1] (if derived[0] == 1)
        first, last = derived[0], derived[0] ^ derived[0]
        for i in range(1, n - 1):
            last = last ^ derived[i]
        if first ^ last == derived[-1]:
            return True
        return False


s = Solution2()
print(s.doesValidArrayExist([1, 0]))
print(s.doesValidArrayExist([1, 1]))
print(s.doesValidArrayExist([1, 1, 0]))
print(s.doesValidArrayExist([1, 1, 0, 0, 0, 0, 0, 1]))
print(s.doesValidArrayExist([1, 1, 0, 0, 1, 1]))
print(s.doesValidArrayExist([1]) is False)
print(s.doesValidArrayExist([0]) is True)