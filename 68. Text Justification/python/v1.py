from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        line = []
        words_in_line = []
        words_len = 0

        while i < len(words):
            words_in_line.append(words[i])
            words_len += len(words[i])
            spaces_len = len(words_in_line) - 1
            total_len = words_len + spaces_len

            if i == len(words) - 1 or total_len + 1 + len(words[i + 1]) > maxWidth:
                if len(words_in_line) == 1 or i == len(words) - 1:
                    res.append(
                        " ".join(words_in_line)
                        + (maxWidth - words_len - (len(words_in_line) - 1)) * " "
                    )
                else:
                    final_spaces_len = maxWidth - words_len
                    min_space_len_per_spot = final_spaces_len // (
                        len(words_in_line) - 1
                    )
                    extra_space = final_spaces_len % (len(words_in_line) - 1)
                    for j, word in enumerate(words_in_line):
                        line.append(word)
                        if j != len(words_in_line) - 1:
                            line.append(
                                " "
                                * (
                                    min_space_len_per_spot
                                    + (1 if extra_space > 0 else 0)
                                )
                            )
                            extra_space -= 1
                    res.append("".join(line))

                line = []
                words_in_line = []
                words_len = 0

            i += 1

        return res
