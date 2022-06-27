# 231. Power of Two
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:

    # 2022/01/23 Scott
    # Time Complexity: O(log(n)) 78.03%
    # Space Complexity: O(log(n)) 42.72%
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 2 or n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)


if __name__ == '__main__':
    s = Solution()

    print(s.isPowerOfTwo(1))
    print(s.isPowerOfTwo(16))
    print(s.isPowerOfTwo(3))
    print(s.isPowerOfTwo(17))
    print(s.isPowerOfTwo(88))
    print(s.isPowerOfTwo(4))
    print(s.isPowerOfTwo(2))
    print(s.isPowerOfTwo(32))