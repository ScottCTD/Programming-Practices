# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
class Solution:

    # Original
    # Not efficient 10.8%
    # Brute Force double loop
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length
        result = 1
        for i in range(length):
            exist = [False] * 128
            exist[ord(s[i])] = True
            temp = 1
            for j in range(i + 1, length):
                if not exist[ord(s[j])]:
                    exist[ord(s[j])] = True
                    temp += 1
                else:
                    break
            if temp > result:
                result = temp
        return result

    # Not original
    # Efficient 92.28%
    # Sliding window
    def lengthOfLongestSubstring2(self, s: str) -> int:
        length = len(s)
        result = 0
        i = 0
        map = {}
        for j in range(length):
            if s[j] in map:
                i = max(map[s[j]], i)
            result = max(result, j - i + 1)
            map[s[j]] = j + 1
        return result

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
    print(Solution().lengthOfLongestSubstring("bbbbb"), 1)
    print(Solution().lengthOfLongestSubstring("pwwkew"), 3)
    print(Solution().lengthOfLongestSubstring(""), 0)
    print(Solution().lengthOfLongestSubstring(" "), 1)
    print(Solution().lengthOfLongestSubstring("au"), 2)

    print("Method 2:")

    print(Solution().lengthOfLongestSubstring2("abcabcbb"), 3)
    print(Solution().lengthOfLongestSubstring2("bbbbb"), 1)
    print(Solution().lengthOfLongestSubstring2("pwwkew"), 3)
    print(Solution().lengthOfLongestSubstring2(""), 0)
    print(Solution().lengthOfLongestSubstring2(" "), 1)
    print(Solution().lengthOfLongestSubstring2("au"), 2)
    print(Solution().lengthOfLongestSubstring2("dvdf"), 3)
    print(Solution().lengthOfLongestSubstring2("abba"), 2)