# Given a string s consisting of small English letters, find and return the first instance of
# a non-repeating character in it. If there is no such character, return '_'.

def solution(s):
    #       count, index
    letters = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
               [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
               [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for j in range(len(s)):
        i = ord(s[j]) - 97
        letters[i][0] += 1
        letters[i][1] = j
    first_index = 10 ** 5
    for count, index in letters:
        if count == 1:
            first_index = min(first_index, index)
    return s[first_index] if first_index != 10 ** 5 else '_'


print(solution('abacabad'))
