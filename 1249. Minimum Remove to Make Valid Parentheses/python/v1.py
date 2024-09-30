class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        list_1 = []
        stack = []
        for i in range(len(s)):
            if s[i] not in ["(", ")"]:
                list_1.append(s[i])
                continue

            if s[i] == "(":
                list_1.append(s[i])
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    continue

                list_1.append(s[i])
                stack.pop()

        list_2 = []
        for i in range(len(list_1) - 1, -1, -1):
            if list_1[i] == "(" and len(stack) != 0:
                stack.pop()
                continue
            list_2.append(list_1[i])

        return "".join(list_2[::-1])
