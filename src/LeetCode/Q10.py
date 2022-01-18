# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


class Solution:

    # Original Scott 4h+
    # Failed Attempt
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)
        i = 0
        j = 0
        while j < n2:
            cp = p[j]
            if cp == '.':
                if j + 1 < n2:
                    next_cp = p[j + 1]
                    if next_cp == '*':
                        j += 1
                        continue
                i += 1
            elif cp == '*':
                prev_cp = p[j - 1]
                if prev_cp == '.':
                    while i <= n1:
                        if self.isMatch(s[i:], p[j + 1:]):
                            return True
                        i += 1
                    return False
                else:
                    if self.isMatch(s[i:], p[j + 1:]):
                            return True
                    while i < n1 and s[i] == prev_cp:
                        if self.isMatch(s[i:], p[j + 1:]):
                            return True
                        i += 1
                    if self.isMatch(s[i:], p[j + 1:]):
                            return True
                    return False
            else:
                if j + 1 < n2:
                    next_cp = p[j + 1]
                    if next_cp == '*':
                        j += 1
                        continue
                if i >= n1:
                    return False
                cs = s[i]
                if cs != cp:
                    return False
                i += 1
            j += 1
        return i == n1

if __name__ == '__main__':
    s = Solution()

    print('1: ' + str(s.isMatch('a', '..'))) # False
    print('2: ' + str(s.isMatch('abc', '.*c'))) # True
    print('3: ' + str(s.isMatch('abc', '.*..'))) # True
    print('4: ' + str(s.isMatch('abc', '.*.'))) # True
    print('5: ' + str(s.isMatch('abc', '.*'))) # True
    print('6: ' + str(s.isMatch('a', '..'))) # False
    print('7: ' + str(s.isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s'))) # True
    print('8: ' + str(s.isMatch('aab', 'c*a*b'))) # True
    print('9: ' + str(s.isMatch('bbcacbabbcbaaccabc', 'b*a*a*.c*bb*b*.*.*'))) # True
    print('10: ' + str(s.isMatch('ccc', 'a*a*a*'))) # False
    print('11: ' + str(s.isMatch('aa', 'a*'))) # True
    print('12: ' + str(s.isMatch('ab', '.*c'))) # False
    print('13: ' + str(s.isMatch('a', 'ab*'))) # True
    print('14: ' + str(s.isMatch('a', '.*..a'))) # False
    print('15: ' + str(s.isMatch('a', '.*..a*'))) # False

