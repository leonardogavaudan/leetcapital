class Solution:
    def maximumSwap(self, num: int) -> int:
        original_num = num
        max_res = num
        max_digit = num % 10
        num //= 10

        current_pos = 1
        max_pos = 0

        while num:
            digit = num % 10
            if digit < max_digit:
                max_res = (
                    original_num
                    + 10**current_pos * (max_digit - digit)
                    + 10**max_pos * (digit - max_digit)
                )
            elif digit > max_digit:
                max_digit = digit
                max_pos = current_pos

            num //= 10
            current_pos += 1

        return max_res
