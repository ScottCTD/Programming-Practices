# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    
    # 2022/01/16 Scott
    # Time Complexity: O(n) 66.50%
    # Space Complexity: O(n)
    def reverseWords(self, s: str) -> str:
        return ' '.join(r[::-1] for r in s.split())

if __name__ == '__main__':
    s = Solution()

    print(s.reverseWords("God Ding"))