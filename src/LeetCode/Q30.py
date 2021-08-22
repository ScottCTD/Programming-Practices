# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。
# 2021/07/23 Scott
# Original
# I covered most cases, but failed at few of them. Then I don't know how to fix that.
class Solution:
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


if __name__ == "__main__":
    print(Solution().findSubstring("barfoothefoobarman", ["bar", "foo"]))
    print([0, 9])
    print(Solution().findSubstring(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    print([])
    print(Solution().findSubstring(
        "barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    print([6, 9, 12])
    print(Solution().findSubstring(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
    print([8])
    print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",
                                   ["fooo", "barr", "wing", "ding", "wing"]))
    print([13])
    print(Solution().findSubstring("a", ["a"]))
    print([0])
    print(Solution().findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"]))
    print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
