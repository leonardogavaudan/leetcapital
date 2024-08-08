class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        i = len(a) - 1
        j = len(b) - 1

        carry = 0

        while i >= 0 or j >= 0:
            sum = carry

            if i >= 0:
                sum += int(a[i])
                i -= 1

            if j >= 0:
                sum += int(b[j])
                j -= 1

            res.append(str(sum % 2))
            carry = sum // 2

        if carry == 1:
            res.append("1")

        return "".join(reversed(res))
