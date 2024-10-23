class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        bitmask = 0
        bitmask_to_position = {0: -1}
        max_length = 0

        for i, c in enumerate(s):
            if c in vowels:
                bitmask ^= 1 << vowels[c]

            if bitmask in bitmask_to_position:
                max_length = max(max_length, i - bitmask_to_position[bitmask])
            else:
                bitmask_to_position[bitmask] = i

        return max_length
