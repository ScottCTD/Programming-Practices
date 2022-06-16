# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
# LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.
# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.
# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".
# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.
# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.

from typing import List, OrderedDict


class Solution:

    def f(self, time_str: str):
        return int(time_str[:2]) * 60 + int(time_str[3:])

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        result = []
        m = [(keyName[i], self.f(keyTime[i])) for i in range(len(keyName))]
        m.sort()
        for i in range(2, len(m)):
            name, time = m[i]
            if result and result[-1] == name:
                continue
            if name == m[i - 2][0] and time - m[i - 2][1] <= 60:
                result.append(name)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.alertNames(["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"], [
          "10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]))
    print(s.alertNames(["alice", "alice", "alice", "bob", "bob", "bob", "bob"], [
          "12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]))
