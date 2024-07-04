class Solution:
    def isValid(self, s: str) -> bool:
        opening_bracket_to_closing_bracket = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in opening_bracket_to_closing_bracket:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if opening_bracket_to_closing_bracket[stack.pop()] != c:
                    return False
        return len(stack) == 0
