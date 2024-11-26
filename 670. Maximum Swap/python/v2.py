class Solution:
    def maximumSwap(self, num: int) -> int:
        res = num
        max_index = 0
        max_digit = num % 10
        original_num = num

        i = 0
        while num:
            digit = num % 10
            if digit > max_digit:
                max_digit = digit
                max_index = i
            else:
                res = max(
                    res,
                    original_num
                    + digit * (10**max_index - 10**i)
                    + max_digit * (10**i - 10**max_index),
                )

            i += 1
            num //= 10

        return res
