class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        special_binary_strings = []

        candidate = []
        zero_count = 0
        for c in s:
            candidate.append(c)
            if c == "0":
                zero_count += 1
            if zero_count == len(candidate) / 2:
                special_str_inside = "".join(candidate[1:-1])
                special_binary_strings.append(
                    "1" + self.makeLargestSpecial(special_str_inside) + "0"
                )
                zero_count = 0
                candidate = []

        return "".join(sorted(special_binary_strings, reverse=True))
