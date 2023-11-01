class Solution:
    def roman_to_integer(self, s: str) -> int:
        roman_to_decimal = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0
        last_char_value = float("inf")

        for roman_char in s:
            if last_char_value < roman_to_decimal[roman_char]:
                res -= last_char_value

            res += roman_to_decimal[roman_char]
            last_char_value = roman_to_decimal[roman_char]

        return int(res)
