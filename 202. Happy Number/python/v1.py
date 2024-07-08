class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            new_value = 0
            while n != 0:
                new_value += (n % 10) ** 2
                n //= 10
            n = new_value

        return True
