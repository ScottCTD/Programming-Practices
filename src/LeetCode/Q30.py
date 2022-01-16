# 30. Substring with Concatenation of All Words
# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.

class Solution:
    # 2021/07/23 Scott
    # Original
    # I covered most cases, but failed at few of them. Then I don't know how to fix that.
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if len(words) == 1:
            if words[0] in s:
                return [s.index(words[0])]
            else:
                return []
        result = []
        map = []
        sLength = len(s)
        wordLength = len(words[0])
        start = 0
        while start < sLength:
            if s[start:start + wordLength] in words:
                for i in range(start, sLength - wordLength + 1, wordLength):
                    j = i + wordLength
                    word = s[i:j]
                    count = words.count(word)
                    if count != 0:
                        indices = []
                        index = -1
                        for k in range(count):
                            index = words.index(word, index + 1)
                            indices.append(index)
                        exist = [False] * len(words)
                        exist[indices[0]] = True
                        map.append([i, exist])
                        if len(map) > 1:
                            for n in range(len(map) - 2, -1, -1):
                                pop = True
                                for k in indices:
                                    if not map[n][1][k]:
                                        map[n][1][k] = True
                                        complete = True
                                        for bool in map[n][1]:
                                            if not bool:
                                                complete = bool
                                                break
                                        if complete:
                                            result.append(map[n][0])
                                            map.pop(n)
                                        pop = False
                                        break
                                if pop:
                                    map.pop(n)
                        start = i
                    else:
                        map.clear()
                        start = i
                        break
            start += 1
        return result

    # 2022/01/15 Scott
    # Original
    # Time Complexity: O(n^2) 73.56%
    # Space Complexity: O(n) 55.75%
    def findSubstring2(self, s: str, words: list[str]) -> list[int]:
        n1 = len(s)
        n2 = len(words[0])
        n3 = len(words) * n2
        result = []
        m = {}
        for word in words:
            if word in m:
                m[word] += 1
            else:
                m[word] = 1

        i = 0
        while i <= n1 - n3:
            s2 = s[i:i + n3]
            if self.is_valid(s2, n2, m.copy()):
                result.append(i)
            i += 1
        return result

    def is_valid(self, s: str, n2: int, m: dict) -> bool:
        for i in range(0, len(s), n2):
            word = s[i:i + n2]
            if word not in m:
                return False
            else:
                if m[word] > 0:
                    m[word] -= 1
                else:
                    return False
        return all(i == 0 for i in m.values())


if __name__ == "__main__":

    s = Solution()

    print(s.findSubstring2('barfoofoobarthefoobarman', ["bar","foo","the"])) # [6, 9, 12]
    print(s.findSubstring2('barfoothefoobarman', ["bar", "foo"])) # [0, 9]
    print(s.findSubstring2('wordgoodgoodgoodbestword', ["word", "good", "best", "word"])) # []
    print(s.findSubstring2('aaaaaaaaaaaaaa', ["aa", "aa"])) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(s.findSubstring2('wordgoodgoodgoodbestword', ["word", "good", "best", "good"])) # [8]
    print(s.findSubstring2('lingmindraboofooowingdingbarrwingmonkeypoundcake', ["fooo", "barr", "wing", "ding", "wing"])) # [13]
    print(s.findSubstring2('a', ["a"])) # [0]
