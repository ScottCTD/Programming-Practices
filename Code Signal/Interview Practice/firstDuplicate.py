# Given an array a that contains only numbers in the range from 1 to a.length,
# find the first duplicate number for which the second occurrence has the minimal index.
# In other words, if there are more than 1 duplicated numbers, return the number for which the
# second occurrence has a smaller index than the second occurrence of the other number does.
# If there are no such elements, return -1.

# 2022-12-25 20:11:23
# partially original
# I struggled for few hours
# I realized that we need to keep the overall structure of the array
# so we cannot sort the array or change the number of 0, for example
# negate the numbers is one way to keep the whole structure unchanged
# but helps to solve the problem in O(1) memory complexity

def solution(a):
    for i in range(len(a)):
        if a[abs(a[i]) - 1] < 0:
            return abs(a[i])
        a[abs(a[i]) - 1] = -a[abs(a[i]) - 1]
    return -1


if __name__ == '__main__':
    print(solution([2, 2]) == 2)
    print(solution([2, 1, 3, 5, 3, 2]) == 3)  # [2, 1, 3, 5, 3, 2]
    print(solution([2, 2, 2, 2, 2]) == 2)
    print(solution([2, 3, 4, 5, 5]) == 5)
    print(solution([5, 4, 3, 2, 1, 1]) == 1)
    print(solution([3, 3, 2, 2, 1, 1]) == 3)
    print(solution([1, 2, 4, 4, 2, 1]) == 4)
    print(solution([2, 2, 2, 4, 2, 1]) == 2)
    print(solution([1, 2, 3, 4, 5, 6]) == -1)
    print(solution([1, 2, 6, 4, 5, 6]) == 6)
    print(solution([1, 2, 6, 4, 4, 6]) == 4)  # [0, 0, 6, 0, 4, 0]
    print(solution([1, 2, 6, 4, 4, 6]) == 4)
    print(solution([1, 1, 6, 4, 4, 6]) == 1)
    print(solution([1, 3, 6, 4, 3, 6]) == 3)
    print(solution([3, 4, 6, 4, 3, 6]) == 4)
    print(solution([3, 3, 6, 6, 3, 6]) == 3)
    print(solution([2, 6, 6, 2, 3, 6]) == 6)  # [2, -6, 6, 2, 3, -6]