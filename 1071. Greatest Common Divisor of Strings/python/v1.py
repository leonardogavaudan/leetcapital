class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        gcd_length = gcd(len(str1), len(str2))
        candidate = str1[:gcd_length]

        if self.verifyDivisor(str1, candidate) and self.verifyDivisor(str2, candidate):
            return candidate
        return ""

    def verifyDivisor(self, s: str, divisor: str) -> bool:
        if len(s) % len(divisor) != 0:
            return False
        return divisor * (len(s) // len(divisor)) == s
