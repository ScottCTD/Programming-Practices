# 541. Reverse String II
# Given a string s and an integer k, 
# reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. 
# If there are less than 2k but greater than or equal to k characters, 
# then reverse the first k characters and left the other as original.
# Scott 2021/08/20

class Solution:

    # Original
    # 72.21%
    def reverseStr(self, s: str, k: int) -> str:
        s_list = [c for c in s]
        l = len(s)
        k2 = k * 2
        remain = l % k2
        for i in range(0, l - remain, k2):
            for j in range(i, i + k // 2, 1):
                index = i + k - 1 - (j - i)
                s_list[j], s_list[index] = s_list[index], s_list[j]
        i = l - remain
        if remain < k:
            for j in range(i, i + remain // 2, 1):
                index = i + remain - 1 - (j - i)
                s_list[j], s_list[index] = s_list[index], s_list[j]
        else:
            for j in range(i, i + k // 2, 1):
                index = i + k - 1 - (j - i)
                s_list[j], s_list[index] = s_list[index], s_list[j]
        
        return ''.join(s_list)


if __name__ == '__main__':
    print(Solution().reverseStr("abcdefg", 2) == "bacdfeg")
    print(Solution().reverseStr("abcd", 2) == "bacd")
    print(Solution().reverseStr("abcdefghijk", 4) == "dcbaefghkji")
    print(Solution().reverseStr("abcdefghigklmnopkrstuvwkya", 5) == "edcbafghigonmlkpkrstykwvua")