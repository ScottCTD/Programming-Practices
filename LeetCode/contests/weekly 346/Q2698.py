# 2698. Find the Punishment Number of an Integer
# Medium
# Given a positive integer n, return the punishment number of n.
#
# The punishment number of n is defined as the sum of the squares of all integers i such that:
#
# 1 <= i <= n
# The decimal representation of i * i can be partitioned into contiguous substrings such that the
# sum of the integer values of these substrings equals i.

# 2023-05-21 01:19:59
# inspired
# learned: when thinking about recursions, firstly find what is the base case
# (how str of length 2 and 1 works)
class Solution:
    def punishmentNumber(self, n: int) -> int:

        # def get_partitions(s):
        #     m = len(s)
        #     if m == 1:
        #         return [[s]]
        #     r = []
        #     for i in range(1, m):
        #         left, right = s[:i], s[i:]
        #         r.extend([left] + right_p for right_p in get_partitions(right))
        #     r.append([s])
        #     return r

        def get_partitions(s):
            m = len(s)
            if m == 1:
                return [int(s)]
            r = []
            for i in range(1, m):
                left, right = s[:i], s[i:]
                r.extend(int(left) + right_p for right_p in get_partitions(right))
            r.append(int(s))
            return r

        r = 0
        for i in range(1, n + 1):
            sq = i ** 2
            sq_str = str(sq)
            partitions = get_partitions(sq_str)
            # for p in partitions:
            #     if sum(map(int, p)) == i:
            #         r += sq
            #         break
            if i in partitions:
                r += sq
        return r


s = Solution()
print(s.punishmentNumber(10) == 182)
print(s.punishmentNumber(37) == 1478)
