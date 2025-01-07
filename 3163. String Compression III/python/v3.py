class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        count = 0
        prev = None

        for c in word:
            if prev and c != prev:
                res.append((count // 9) * f"9{prev}")
                res.append(f"{count % 9}{prev}" if count % 9 else "")
                count = 0
            prev = c
            count += 1

        res.append((count // 9) * f"9{prev}")
        res.append(f"{count % 9}{prev}" if count % 9 else "")

        return "".join(res)
