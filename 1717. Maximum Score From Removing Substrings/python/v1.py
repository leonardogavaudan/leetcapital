class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        stack_1 = []

        for c in s:
            if c == "b" and x >= y:
                if stack_1 and stack_1[-1] == "a":
                    stack_1.pop()
                    res += x
                    continue
            if c == "a" and x < y:
                if stack_1 and stack_1[-1] == "b":
                    stack_1.pop()
                    res += y
                    continue

            stack_1.append(c)

        stack_2 = []

        for c in stack_1:
            if c == "a" and x >= y:
                if stack_2 and stack_2[-1] == "b":
                    stack_2.pop()
                    res += y
                    continue
            if c == "b" and x < y:
                if stack_2 and stack_2[-1] == "a":
                    stack_2.pop()
                    res += x
                    continue

            stack_2.append(c)

        return res
