class Solution:
    def nearestPalindromic(self, n: str) -> str:
        candidates = [
            10 ** (len(n) - 1) - 1,
            10 ** len(n) + 1,
        ]

        prefix = int(n[: (len(n) + 1) // 2])
        for offset in [-1, 0, 1]:
            new_prefix_str = str(prefix + offset)
            to_add = new_prefix_str[:-1] if len(n) % 2 else new_prefix_str
            candidates.append(int(new_prefix_str + to_add[::-1]))

        if int(n) in candidates:
            candidates.remove(int(n))

        return str(min(candidates, key=lambda x: abs(int(n) - x)))
