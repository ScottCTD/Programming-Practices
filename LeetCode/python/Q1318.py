# 1318. Minimum Flips to Make a OR b Equal to c
# Medium
# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b
# to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary
# representation.


# 2023-06-06 22:52:35
# original (almost)
# time O(n) space O(1)
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            # bina = bin(a)
            # binb = bin(b)
            # binc = bin(c)
            if c & 1:
                ans += not (a & 1 | b & 1)
            else:
                ans += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return ans


s = Solution()
print(s.minFlips(2, 6, 5))
print(s.minFlips(2, 3, 100))
print(s.minFlips(8, 3, 5))