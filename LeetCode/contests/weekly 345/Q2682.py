from typing import List

# 2023-05-14 00:51:20
# contest question
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        j = 0
        i = 0
        m = 0
        a = [0] * n

        a[0] = 1
        i += 1
        m += (k * i) % n
        while True:
            a[m] += 1
            if a[m] == 2:
                break
            i += 1
            m = (m + k * i) % n
        res = []
        for i in range(n):
            if a[i] == 0:
                res.append(i + 1)
        return res


s = Solution()
print(s.circularGameLosers(5, 2))
print(s.circularGameLosers(12, 1))

