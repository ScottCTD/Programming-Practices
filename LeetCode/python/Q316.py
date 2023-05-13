# 316. Remove Duplicate Letters
# Given a string s, remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order
# among all possible results.

class Solution:

    # 2023-05-12 23:32:21
    # half-original
    # monotonic stack
    # time 16.95% space 21.47%
    # however, the time complexity is O(n) and space complexity is O(n) in the average case
    # so it's okay
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []
        visited = set()
        last_occ = {}
        for i in range(n):
            last_occ[s[i]] = i
        for i in range(n):
            if s[i] in visited:
                continue
            while stack and stack[-1] > s[i] and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(s[i])
            visited.add(s[i])
        return ''.join(stack)


s = Solution()
print(s.removeDuplicateLetters('bcabc'))
print(s.removeDuplicateLetters('cbacdcbc'))