class Solution:
    def maximumSwap(self, num: int) -> int:
        original_num = num
        res = num
        max_digit = -1
        max_index = -1
        index = 0

        while num:
            lsd = num % 10
            if lsd < max_digit:
                res = (
                    original_num
                    + lsd * (10**max_index - 10**index)
                    + max_digit * (10**index - 10**max_index)
                )
            elif lsd > max_digit:
                max_digit = lsd
                max_index = index

            num //= 10
            index += 1

        return res
