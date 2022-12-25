# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for
# '.' and '*' where:
from typing import Any, Callable


# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


class Solution:

    # Original Scott 4h+
    # Failed Attempt
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)
        i = 0
        j = 0
        while j < n2:
            cp = p[j]
            if cp == '.':
                if j + 1 < n2:
                    next_cp = p[j + 1]
                    if next_cp == '*':
                        j += 1
                        continue
                i += 1
            elif cp == '*':
                prev_cp = p[j - 1]
                if prev_cp == '.':
                    while i <= n1:
                        if self.isMatch(s[i:], p[j + 1:]):
                            return True
                        i += 1
                    return False
                else:
                    if self.isMatch(s[i:], p[j + 1:]):
                        return True
                    while i < n1 and s[i] == prev_cp:
                        if self.isMatch(s[i:], p[j + 1:]):
                            return True
                        i += 1
                    if self.isMatch(s[i:], p[j + 1:]):
                        return True
                    return False
            else:
                if j + 1 < n2:
                    next_cp = p[j + 1]
                    if next_cp == '*':
                        j += 1
                        continue
                if i >= n1:
                    return False
                cs = s[i]
                if cs != cp:
                    return False
                i += 1
            j += 1
        return i == n1


class State:
    is_accepting: bool
    transitions: list

    def __init__(self, is_accepting: bool, transitions: list) -> None:
        self.is_accepting = is_accepting
        self.transitions = transitions


class Transition:
    next_state: State
    symbol: str

    def __init__(self, next_state: State, symbol: str) -> None:
        self.next_state = next_state
        self.symbol = symbol


# 2022-12-24 19:41:20
# an original working solution
# the running time is a disaster: beats 13.53%
# memory beats 6.46%
class Solution2:

    def create_NFA(self, p: str) -> State:
        n = len(p)
        initial_state = State(False, [])
        state = initial_state
        i = 0
        while i < n:
            c = p[i]
            if c == '.':
                if i == n - 1:
                    next_state = State(True, [])
                    state.transitions.append(Transition(next_state, '.'))
                else:
                    if p[i + 1] == '*':
                        next_state = State(i + 1 == n - 1, [])
                        next_state.transitions.append(Transition(next_state, '.'))
                        state.transitions.append(Transition(next_state, ''))
                        state = next_state
                        i += 1
                    else:
                        next_state = State(False, [])
                        state.transitions.append(Transition(next_state, '.'))
                        state = next_state
            else:  # a letter
                if i == n - 1:
                    next_state = State(True, [])
                    state.transitions.append(Transition(next_state, c))
                else:
                    if p[i + 1] == '*':
                        next_state = State(i + 1 == n - 1, [])
                        next_state.transitions.append(Transition(next_state, c))
                        state.transitions.append(Transition(next_state, ''))
                        state = next_state
                        i += 1
                    else:
                        next_state = State(False, [])
                        state.transitions.append(Transition(next_state, c))
                        state = next_state
            i += 1
        return initial_state

    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        nfa = self.create_NFA(p)
        current_states = [nfa]
        for i in range(n):
            c = s[i]
            new_states = []
            any_match = False
            while current_states:
                state = current_states.pop()
                for transition in state.transitions:
                    if transition.symbol == c or transition.symbol == '.':
                        any_match = True
                        next_state = transition.next_state
                        if next_state.is_accepting and i == n - 1:
                            return True
                        new_states.append(next_state)
                    if transition.symbol == '':
                        current_states.append(transition.next_state)
            current_states = new_states
            if not any_match:
                return False
        while current_states:
            state = current_states.pop()
            if state.is_accepting:
                return True
            for transition in state.transitions:
                if transition.symbol == '':
                    current_states.append(transition.next_state)
        return False


if __name__ == '__main__':
    solution = Solution()

    print('1: ' + str(solution.isMatch('a', '..')))  # False
    print('2: ' + str(solution.isMatch('abc', '.*c')))  # True
    print('3: ' + str(solution.isMatch('abc', '.*..')))  # True
    print('4: ' + str(solution.isMatch('abc', '.*.')))  # True
    print('5: ' + str(solution.isMatch('abc', '.*')))  # True
    print('6: ' + str(solution.isMatch('a', '..')))  # False
    print('7: ' + str(solution.isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s')))  # T
    print('8: ' + str(solution.isMatch('aab', 'c*a*b')))  # True
    print('9: ' + str(solution.isMatch('bbcacbabbcbaaccabc', 'b*a*a*.c*bb*b*.*.*')))  # True
    print('10: ' + str(solution.isMatch('ccc', 'a*a*a*')))  # False
    print('11: ' + str(solution.isMatch('aa', 'a*')))  # True
    print('12: ' + str(solution.isMatch('ab', '.*c')))  # False
    print('13: ' + str(solution.isMatch('a', 'ab*')))  # True
    print('14: ' + str(solution.isMatch('a', '.*..a')))  # False
    print('15: ' + str(solution.isMatch('a', '.*..a*')))  # False

    solution = Solution2()
    print('1: ' + str(solution.isMatch('a', '..') is False))  # False
    print('2: ' + str(solution.isMatch('abc', '.*c') is True))  # True
    print('3: ' + str(solution.isMatch('abc', '.*..') is True))  # True
    print('4: ' + str(solution.isMatch('abc', '.*.') is True))  # True
    print('5: ' + str(solution.isMatch('abc', '.*') is True))  # True
    print('6: ' + str(solution.isMatch('a', '..') is False))  # False
    print('7: ' + str(solution.isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s') is True))  # T
    print('8: ' + str(solution.isMatch('aab', 'c*a*b') is True))  # True
    print('9: ' + str(solution.isMatch('bbcacbabbcbaaccabc', 'b*a*a*.c*bb*b*.*.*') is True))  # True
    print('10: ' + str(solution.isMatch('ccc', 'a*a*a*') is False))  # False
    print('11: ' + str(solution.isMatch('aa', 'a*') is True))  # True
    print('12: ' + str(solution.isMatch('ab', '.*c') is False))  # False
    print('13: ' + str(solution.isMatch('a', 'ab*') is True))  # True
    print('14: ' + str(solution.isMatch('a', '.*..a') is False))  # False
    print('15: ' + str(solution.isMatch('a', '.*..a*') is False))  # False
    print('16: ' + str(solution.isMatch('aas', 'a.*a.*s') is True))  # True
    print('17: ' + str(solution.isMatch('aa', 'a') is False))  # False
    print('18: ' + str(solution.isMatch('abcaaaaaaabaabcabac', '.*ab.a.*a*a*.*b*b*') is True))