class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        largest_number_seen = roman_to_int[s[-1]]
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if roman_to_int[s[i]] > largest_number_seen:
                largest_number_seen = roman_to_int[s[i]]

            if roman_to_int[s[i]] >= largest_number_seen:
                res += roman_to_int[s[i]]
            else:
                res -= roman_to_int[s[i]]

        return res
