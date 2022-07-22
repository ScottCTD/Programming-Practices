# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:

    # a failed attempt of double index
    def backspaceCompare(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        i, j = 0, 0
        while i < n1 or j < n2:
            sb = i
            while i < n1 and s[i] != '#':
                i += 1
            se = i
            while i < n1 and s[i] == '#':
                i += 1
            se -= i - se
            # now s[sb, se] is the range for real comparing
            # then we do the same thing for t
            tb = j
            while j < n2 and t[j] != '#':
                j += 1
            te = j
            while j < n2 and t[j] == '#':
                j += 1
            te -= j - te

            if sb == se and tb != te or tb == te and sb != se:
                continue
            # check if they are equal
            if s[sb:se] != t[tb:te]:
                return False

        return i == n1 and j == n2

    # learned
    # double index starting from tail
    # iterate through each character one by one, **no block skip or comparison**
    def backspaceCompare2(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        i, j = n1 - 1, n2 - 1
        while i >= 0 or j >= 0:
            skip = 0
            while i >= 0:
                if s[i] == '#':
                    skip += 1
                    i -= 1
                elif skip > 0:
                    skip -= 1
                    i -= 1
                else:
                    break
            skip = 0
            while j >= 0:
                if t[j] == '#':
                    skip += 1
                    j -= 1
                elif skip > 0:
                    skip -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            else:
                if i >= 0 or j >= 0:
                    return False

            i -= 1
            j -= 1
        return True


s = Solution()
print(s.backspaceCompare2("ab#c", "ad#c"))
print(s.backspaceCompare2("ab##", "c#d#"))
print(s.backspaceCompare2("a#c", "b"))
print(s.backspaceCompare2("abcd####a#jdwiodjioa#jw###", "abcd####a#jdwiodjia#"))
print(s.backspaceCompare2("a#c###", "ad#c"))
