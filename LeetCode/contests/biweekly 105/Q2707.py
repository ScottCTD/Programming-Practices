

from typing import List, Optional
from collections import deque, defaultdict


# 2023-05-27 12:05:56
# original
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [-1] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for d in dictionary:
                m = len(d)
                if s[i - m:i] == d:
                    if dp[i] == -1:
                        dp[i] = min(dp[i - m], dp[i - 1] + 1)
                    else:
                        dp[i] = min(dp[i], dp[i - m])
                    # print(s[i - m:i])
                    # print(dp[i])
            if dp[i] == -1:
                dp[i] = dp[i - 1] + 1
        return dp[n]



s = Solution()
print(s.minExtraChar('leetscode', ["leet","code","leetcode"]))
print(s.minExtraChar('abbaabb', ["ab","ba","abb"]))
print(s.minExtraChar('bbbbbbba', ["ab","ba","abb", 'a']))
print(s.minExtraChar('ababbab', ["ab","ba","abb", 'a']))
print(s.minExtraChar('abcdacaede', ["a","b","c", 'd']))
print(s.minExtraChar('kevlplxozaizdhxoimmraiakbak',
                     ["yv","bmab","hv","bnsll","mra","jjqf","g","aiyzi",
                      "ip","pfctr","flr","ybbcl","biu","ke","lpl","iak",
                      "pirua","ilhqd","zdhx","fux","xaw","pdfvt","xf",
                      "t","wq","r","cgmud","aokas","xv","jf","cyys","wcaz",
                      "rvegf","ysg","xo","uwb","lw","okgk","vbmi","v","mvo","fxyx","ad","e"]))
print(s.minExtraChar('zdhxo', ['zdhx', 'xo']))