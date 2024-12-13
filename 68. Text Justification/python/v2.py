from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        words_line = []
        words_len = 0

        for word in words:
            if (words_len + len(words_line) + len(word)) > maxWidth:
                if len(words_line) == 1:
                    res.append(words_line[0] + " " * (maxWidth - words_len))
                else:
                    line = []
                    remaining_space = maxWidth - words_len
                    for i, w in enumerate(words_line[:-1]):
                        line.append(
                            w
                            + " "
                            * (
                                remaining_space // (len(words_line) - 1)
                                + (
                                    1
                                    if i < remaining_space % (len(words_line) - 1)
                                    else 0
                                )
                            )
                        )
                    line.append(words_line[-1])
                    res.append("".join(line))

                words_line = []
                words_len = 0

            words_line.append(word)
            words_len += len(word)

        res.append(
            " ".join(words_line) + " " * (maxWidth - words_len - (len(words_line) - 1))
        )

        return res
