# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Scott 2022/01/15

class Solution:

    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    cm = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        """
        Time Complexity: O(n) 96.64%
        Space Complexity: O(1) 5.04%   
        """
        n = len(s)
        result = 0
        i = 0
        while i < n - 1:
            c = s[i]
            cc = s[i] + s[i + 1]
            if cc in self.cm:
                result += self.cm[cc]
                i += 1
            else:
                result += self.m[c]
            i += 1
        if i == n - 1:
            result += self.m[s[-1]]
        return result


if __name__ == '__main__':
    s = Solution()

    print(s.romanToInt('MCMXCIV'))
    print(s.romanToInt('MDCXCV'))