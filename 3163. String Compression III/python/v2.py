class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        count = 0
        prev_char = word[0]
        for i, c in enumerate(word):
            if c == prev_char:
                count += 1
            else:
                res.append(
                    f"{f'9{prev_char}' * (count // 9)}{f'{count % 9}{prev_char}' if count % 9 else ''}"
                )
                count = 1

            if i == len(word) - 1:
                res.append(
                    f"{f'9{c}' * (count // 9)}{f'{count % 9}{c}' if count % 9 else ''}"
                )

            prev_char = c

        return "".join(res)
