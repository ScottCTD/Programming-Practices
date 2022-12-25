# 44. Wildcard Matching
# Given an input string (s) and a pattern (p),
# implement wildcard pattern matching with support for '?' and '*' where:
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).


# 2022-12-25 12:27:35
# an original but not efficient solution
# RT: 2441 ms beats 10.79%
# MEM: 14.6 ms beats 76.96%
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        transitions: dict[tuple[int, str], set[int]] = {}
        accepting_state = 0
        # construct the NFA
        np = len(p)
        i = 0
        state = 0
        while i < np:
            c = p[i]
            if c == '*':
                transitions[(state, '?')] = {state}
                transitions[(state, '')] = {state + 1}
                state += 1
            elif c == '?':
                transitions[(state, '?')] = {state + 1}
                state += 1
            else:
                transitions[(state, c)] = {state + 1}
                state += 1
            if i == np - 1:
                accepting_state = state
            i += 1

        print(transitions)
        print(accepting_state)

        # match s with NFA
        i = 0
        ns = len(s)
        current_states = {0}
        while i < ns:
            c = s[i]
            new_states = set()
            while current_states:
                state = current_states.pop()
                # handle epsilons
                epsilons = {(state, '')}
                while epsilons:
                    epsilon = epsilons.pop()
                    if epsilon in transitions:
                        next_states = transitions[epsilon]
                        current_states = current_states.union(next_states)
                        epsilons = epsilons.union((next_state, '') for next_state in next_states)
                # other cases
                a = (state, c)
                if a in transitions:
                    new_states = new_states.union(transitions[a])
                    continue
                a = (state, '?')
                if a in transitions:
                    new_states = new_states.union(transitions[a])
                    continue
            if i == ns - 1 and accepting_state in current_states:
                return True
            current_states = new_states
            i += 1
        while current_states:
            if accepting_state in current_states:
                return True
            a = (current_states.pop(), '')
            if a in transitions:
                current_states = current_states.union(transitions[a])
        return False


if __name__ == '__main__':
    solution = Solution()
    print(f"1. {solution.isMatch('abc', 'a*c') is True}")