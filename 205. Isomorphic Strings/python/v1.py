class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_to_new_char = {}
        chars_mapped_to = set()

        for i in range(len(s)):
            if s[i] in char_to_new_char:
                if t[i] != char_to_new_char[s[i]]:
                    return False
            else:
                if t[i] in chars_mapped_to:
                    return False
                char_to_new_char[s[i]] = t[i]
                chars_mapped_to.add(t[i])

        return True
