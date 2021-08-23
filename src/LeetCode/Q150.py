# 150. Evaluate Reverse Polish Notation
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
# Note that division between two integers should truncate toward zero.
# It is guaranteed that the given RPN expression is always valid.
# That means the expression would always evaluate to a result,
# and there will not be any division by zero operation.
# Scott 2021/08/23

from typing import List
import collections


class Solution:

    # Original
    # 89.70%
    # Time O(n)
    # Space O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif item == '-':
                last = int(stack.pop())
                second_last = int(stack.pop())
                stack.append(second_last - last)
            elif item == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif item == '/':
                last = int(stack.pop())
                second_last = int(stack.pop())
                stack.append(int(second_last / last))
            else:
                stack.append(item)
        return int(stack[0])


if __name__ == '__main__':
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
    print(Solution().evalRPN(["10", "6", "9", "3",
          "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

