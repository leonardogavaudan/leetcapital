class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [word for word in s.split(" ") if word]
        return " ".join(arr[::-1])
