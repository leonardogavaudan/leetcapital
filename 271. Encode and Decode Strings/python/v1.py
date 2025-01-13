from typing import List


class Codec:
    DELIMITER = "|"
    ESCAPE_CHAR = "\\"

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            s = s.replace(self.ESCAPE_CHAR, 2 * self.ESCAPE_CHAR)
            s = s.replace(self.DELIMITER, self.ESCAPE_CHAR + self.DELIMITER)
            parts.append(s + self.DELIMITER)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        decoded = []
        current = []
        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if ch == self.ESCAPE_CHAR:
                if i + 1 >= n:
                    raise ValueError("Invalid encoding")
                next_ch = s[i + 1]
                current.append(next_ch)
                i += 2
            elif ch == self.DELIMITER:
                decoded.append("".join(current))
                current = []
                i += 1
            else:
                current.append(ch)
                i += 1
        if current:
            raise ValueError("Invalid encoding")
        return decoded
