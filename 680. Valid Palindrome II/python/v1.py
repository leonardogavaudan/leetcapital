class Solution:
    def validPalindrome(self, s: str) -> bool:
        arr = list(s)
        while len(arr) > 1:
            left_char = arr.pop(0)
            right_char = arr.pop()

            if left_char == right_char:
                continue

            return self.isValidPalindrome(
                left_char + "".join(arr)
            ) or self.isValidPalindrome("".join(arr) + right_char)

        return True

    def isValidPalindrome(self, s: str) -> bool:
        arr = list(s)
        while len(arr) > 1:
            if arr.pop(0) != arr.pop():
                return False
        return True
