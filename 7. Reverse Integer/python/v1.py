class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        res = 0

        while x:
            digit = x % 10
            x //= 10
            res = res * 10 + digit

            if res > 2**31 - 1:
                return 0

        return res if not negative else -res
