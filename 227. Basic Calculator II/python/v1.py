class Solution:
    def process(self, x1: int, x2: int, operator: str):
        if operator == "+":
            return x1 + x2
        if operator == "-":
            return x1 - x2
        if operator == "*":
            return x1 * x2
        else:
            return int(x1 / x2)

    def calculate(self, s: str) -> int:
        operators = set(["+", "-", "*", "/"])

        def move_to_operator(x: int):
            while x < len(s) and s[x] not in operators:
                x += 1
            return x

        is_neg = s[0] == "-"
        first_index = 1 if is_neg else 0
        i = move_to_operator(first_index)
        operand1 = -int(s[first_index:i]) if is_neg else int(s[first_index:i])
        if i == len(s):
            return operand1
        operator1 = s[i]

        j = move_to_operator(i + 1)
        operand2 = int(s[i + 1 : j])
        if j == len(s):
            return self.process(operand1, operand2, operator1)

        operator2 = s[j]

        while j < len(s):
            if operator1 in ["*", "/"] or operator2 in ["+", "-"]:
                operand1 = self.process(operand1, operand2, operator1)
                operator1 = operator2
                i = j
                j = move_to_operator(j + 1)
                operand2 = int(s[i + 1 : j])
                if j == len(s):
                    return self.process(operand1, operand2, operator1)
                operator2 = s[j]
            else:
                k = move_to_operator(j + 1)
                operand3 = int(s[j + 1 : k])
                operand2 = self.process(operand2, operand3, operator2)
                if k == len(s):
                    return self.process(operand1, operand2, operator1)
                operator2 = s[k]
                j = k

        return self.process(operand1, operand2, operator1)
