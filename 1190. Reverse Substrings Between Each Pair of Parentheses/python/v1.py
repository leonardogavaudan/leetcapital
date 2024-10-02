class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ")":
                temp_list = []
                while stack[-1] != "(":
                    temp_list.append(stack.pop())
                stack.pop()
                stack.extend(temp_list)
            else:
                stack.append(c)

        return "".join(stack)
