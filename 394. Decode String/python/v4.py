class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                to_mulitiply = []
                while stack[-1] != "[":
                    to_mulitiply.append(stack.pop())
                stack.pop()

                multiplier = 0
                power = 1
                while stack and stack[-1].isdigit():
                    multiplier = multiplier + int(stack.pop()) * power
                    power *= 10
                stack.extend(to_mulitiply[::-1] * multiplier)

        return "".join(stack)
