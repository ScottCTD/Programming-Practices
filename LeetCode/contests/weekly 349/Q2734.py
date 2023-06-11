# 2023-06-11 01:07:21
# original
class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        i, j = 0, 0
        while i < n and s[i] == 'a':
            i += 1
        if i == n:
            return s[:n - 1] + 'z'
        j = i + 1
        while j < n and s[j] != 'a':
            j += 1
        ans = list(s)
        for k in range(i, j):
            ans[k] = chr(ord(s[k]) - 1)
        return ''.join(ans)


s = Solution()
print(s.smallestString('cbabc'))
print(s.smallestString('acbbc'))
print(s.smallestString('leetcode'))
