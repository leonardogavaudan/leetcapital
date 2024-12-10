class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        i = 0
        count = 0
        char = word[0]

        while i < len(word):
            if word[i] != char:
                res.append(
                    f"9{char}" * (count // 9)
                    + (f"{count % 9}{char}" if count % 9 else "")
                )
                count = 0
                char = word[i]
            count += 1
            i += 1

        res.append(
            f"9{char}" * (count // 9) + (f"{count % 9}{char}" if count % 9 else "")
        )

        return "".join(res)
