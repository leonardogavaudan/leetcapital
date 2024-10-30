class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0
        bitmask = 0
        shift = {chr(ord("a") + i): i for i in range(10)}
        bitmask_to_count = {0: 1}

        for char in word:
            if char in shift:
                bitmask ^= 1 << shift[char]

            res += bitmask_to_count.get(bitmask, 0)

            for i in range(32):
                new_bitmask = bitmask ^ (1 << i)
                res += bitmask_to_count.get(new_bitmask, 0)

            if bitmask not in bitmask_to_count:
                bitmask_to_count[bitmask] = 0
            bitmask_to_count[bitmask] += 1

        return res
