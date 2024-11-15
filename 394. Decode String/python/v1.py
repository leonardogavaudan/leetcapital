class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        stack = []
        stack_multiplier = []
        current = []
        i = 0
        while i < len(s):
            if not stack and not s[i].isdigit() and s not in ["[", "]"]:
                res.append(s[i])
                i += 1
                continue

            if s[i].isdigit():
                stack.append(current)
                current = []

                start = i
                while s[i].isdigit():
                    i += 1
                multiplier = int(s[start:i])
                stack_multiplier.append(multiplier)
                i += 1
                continue

            if s[i] == "]":
                current = stack_multiplier.pop() * current
                current = stack.pop() + current
                if not stack:
                    res.append("".join(current))
                    current = []
                i += 1
                continue

            current.append(s[i])
            i += 1

        return "".join(res)
