class Solution:
    def fib(self, n: int) -> int:
        n1, n2 = 0, 1

        for _ in range(n):
            temp = n1 + n2
            n1 = n2
            n2 = temp

        return n1
