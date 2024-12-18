class Solution:
    def nearestPalindromic(self, n: str) -> str:
        candidates = set(
            [
                str(10 ** (len(n) - 1) - 1),
                str(10 ** len(n) + 1),
            ]
        )
        first_half = n[: (len(n) + 1) // 2]

        for offset in [-1, 0, 1]:
            new_half_int = int(first_half) + offset
            new_half = str(new_half_int)
            candidates.add(
                (new_half if len(n) % 2 == 0 else new_half[:-1]) + new_half[::-1]
            )

        candidates.discard(n)

        return min(candidates, key=lambda s: (abs(int(n) - int(s)), int(s)))
