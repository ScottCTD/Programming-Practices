# 2024. Maximize the Confusion of an Exam
# Medium
# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting
# false. He wants to confuse the students by maximizing the number of consecutive questions with
# the same answer (multiple trues or multiple falses in a row).
#
# You are given a string answerKey, where answerKey[i] is the original answer to the ith question.
# In addition, you are given an integer k, the maximum number of times you may perform the following
# operation:
#
# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the
# operation at most k times.
from collections import Counter


# 2023-07-06 21:08:31
# learned
# sliding window
# 状态差 GGGGG
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        count = Counter(answerKey[:k])
        start = 0
        ans = k
        for i in range(k, n):
            ans = max(ans, i - start)
            count[answerKey[i]] += 1
            # while we cannot flip the answers in the window
            while min(count['T'], count['F']) > k:
                count[answerKey[start]] -= 1
                start += 1
        return max(ans, n - start)


s = Solution()
print(s.maxConsecutiveAnswers('TTFF', 2))  # 4
print(s.maxConsecutiveAnswers('TFFT', 1))  # 3
print(s.maxConsecutiveAnswers('TTFTTFTT', 1))  # 5
print(s.maxConsecutiveAnswers('TTFTTTTTFT', 1))  # 8
