# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.

class Solution:

    # Original
    # 96.99%
    def countCharacters(self, words: list[str], chars: str) -> int:
        result = 0
        char_map = {}
        for c in chars:
            if c in char_map:
                char_map[c] += 1
            else:
                char_map[c] = 1
        for s in words:
            good = True
            temp = char_map.copy()
            for c in s:
                if c not in temp:
                    good = False
                    break
                elif temp[c] == 1:
                    del temp[c]
                else:
                    temp[c] -= 1
            if good:
                result += len(s)
        return result


if __name__ == "__main__":
    print(Solution().countCharacters(
        ["cat", "bt", "hat", "tree"], "atach") == 6)
    print(Solution().countCharacters(
        ["hello", "world", "leetcode"], "welldonehoneyr") == 10)
