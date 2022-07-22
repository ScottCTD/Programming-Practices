# Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n
# Failed because reach maximum recursive calls
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            if n > 1:
                return x * self.myPow(x, n - 1)
            else:
                return x
        elif n < 0:
            return self.myPow(1 / x, -n)
        elif n == 0:
            return 1


if __name__ == '__main__':
    print(0.00001 ** 2147483647)
    print(Solution().myPow(2, 10), 1024)
    print(Solution().myPow(2.1, 3), 9.261)
    print(Solution().myPow(2, -2), 0.25)
    print(Solution().myPow(100, -20), 100 ** -20)
    print(Solution().myPow(0.44528, 0), 0.44528 ** 0)
    print(Solution().myPow(0.00001, 2147483647), 0.00001 ** 2147483647)
