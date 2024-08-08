class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0

        while i >= 0 or j >= 0:
            sum = carry

            if i >= 0:
                sum += int(num1[i])

            if j >= 0:
                sum += int(num2[j])

            res.append(str(sum % 10))
            carry = sum // 10

            i -= 1
            j -= 1

        if carry == 1:
            res.append("1")

        return "".join(res[::-1])
