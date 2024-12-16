class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s

        special_strs = []
        i = 0
        start = 0
        count = 0
        while i < len(s):
            if s[i] == "0":
                count += 1

            current_len = i - start + 1
            if count == current_len / 2:
                special_strs.append(
                    "1" + self.makeLargestSpecial(s[start + 1 : i]) + "0"
                )
                start = i + 1
                count = 0

            i += 1

        special_strs.sort(reverse=True)

        return "".join(special_strs)
