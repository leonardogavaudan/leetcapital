class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            if n % 2 == 1:
                res = res * x
                n -= 1
                if n == 0:
                    break

            x = x**2
            n = n // 2

        return res