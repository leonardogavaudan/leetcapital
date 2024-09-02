class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s_list = list(s)

        while l < len(s_list) and r > 0:
            while l < len(s_list) and s_list[l] not in vowels:
                l += 1
            while r > 0 and s_list[r] not in vowels:
                r -= 1

            if l >= r:
                break

            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1

        return "".join(s_list)
