class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s):
            if s[i] != "]":
                stack.append(s[i])
                i += 1
                continue

            popped_str = []
            while stack[-1] != "[":
                popped_str.append(stack.pop())
            popped_str = popped_str[::-1]
            stack.pop()

            mult = 0
            pow = 0
            while stack and stack[-1].isdigit():
                mult = mult + int(stack.pop()) * 10**pow
                pow += 1
            stack.extend(mult * popped_str)

            i += 1

        return "".join(stack)
