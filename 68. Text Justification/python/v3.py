from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line_words_len = 0
        line_words = []

        for word in words:
            if line_words_len + len(line_words) + len(word) > maxWidth:
                if len(line_words) == 1:
                    res.append(line_words[0] + " " * (maxWidth - len(line_words[0])))
                else:
                    spaces_count = maxWidth - line_words_len
                    line_res = []
                    base_space = spaces_count // (len(line_words) - 1)
                    for i, line_word in enumerate(line_words[:-1]):
                        line_res.append(line_word)
                        line_res.append(
                            " "
                            * (
                                base_space
                                + (1 if i < spaces_count % (len(line_words) - 1) else 0)
                            )
                        )
                    line_res.append(line_words[-1])
                    res.append("".join(line_res))

                line_words = []
                line_words_len = 0

            line_words.append(word)
            line_words_len += len(word)

        res.append(
            " ".join(line_words)
            + " " * (maxWidth - (line_words_len + len(line_words) - 1))
        )

        return res
