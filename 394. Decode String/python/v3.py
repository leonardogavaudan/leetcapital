class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                word = []
                while stack[-1] != "[":
                    word.append(stack.pop())

                stack.pop()

                mult = 0
                i = 0
                while stack and stack[-1].isdigit():
                    mult += int(stack.pop()) * 10**i
                    i += 1

                stack.extend(word[::-1] * mult)
            else:
                stack.append(char)

        return "".join(stack)
