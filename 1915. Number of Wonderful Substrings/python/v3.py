class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0
        mask_to_count = {0: 1}
        mask = 0

        for c in word:
            mask ^= 1 << (ord(c) - ord("a"))
            res += mask_to_count.get(mask, 0)

            for i in range(10):
                modified_mask = mask ^ 1 << i
                res += mask_to_count.get(modified_mask, 0)

            if mask not in mask_to_count:
                mask_to_count[mask] = 0

            mask_to_count[mask] += 1

        return res
