class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False

                skip_count = 0
                while j < len(abbr) and abbr[j].isdigit():
                    skip_count = skip_count * 10 + int(abbr[j])
                    j += 1

                i += skip_count
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)
