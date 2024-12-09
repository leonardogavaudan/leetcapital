class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        subs = []
        count = 0
        start = 0
        for i, ch in enumerate(s):
            count += 1 if ch == "1" else -1
            if count == 0:
                subs.append("1" + self.makeLargestSpecial(s[start + 1 : i]) + "0")
                start = i + 1
        subs.sort(reverse=True)
        return "".join(subs)
