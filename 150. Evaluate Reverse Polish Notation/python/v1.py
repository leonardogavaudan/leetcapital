from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] in "+-*/":
                stack.append(tokens[i])
                continue

            operand1 = int(tokens[i])
            while len(stack) > 1 and stack[-1] not in "+-*/":
                operand2 = int(stack.pop())
                operator = stack.pop()
                if operator == "+":
                    operand1 = operand1 + operand2
                if operator == "-":
                    operand1 = operand1 - operand2
                if operator == "*":
                    operand1 = operand1 * operand2
                if operator == "/":
                    operand1 = int(operand1 / operand2)

            stack.append(str(operand1))

        return int(stack[0])
