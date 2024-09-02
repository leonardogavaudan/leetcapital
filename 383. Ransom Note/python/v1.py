class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_to_count = {}

        for c in magazine:
            if c not in letter_to_count:
                letter_to_count[c] = 0

            letter_to_count[c] += 1

        for c in ransomNote:
            if c not in letter_to_count:
                return False

            letter_to_count[c] -= 1
            if letter_to_count[c] == 0:
                del letter_to_count[c]

        return True
