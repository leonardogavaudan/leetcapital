from collections import deque


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        units = ["", "Thousand", "Million", "Billion"]
        digit_to_regular = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        decimals = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        irregulars = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        def process_triplet(triplet):
            result = []
            if triplet >= 100:
                result.append(digit_to_regular[triplet // 100])
                result.append("Hundred")
            remainder = triplet % 100
            if remainder in irregulars:
                result.append(irregulars[remainder])
            else:
                if remainder >= 20:
                    result.append(decimals[remainder // 10])
                    remainder %= 10
                if remainder > 0:
                    result.append(digit_to_regular[remainder])
            return result

        res = deque()
        unit_index = 0

        while num > 0:
            triplet = num % 1000
            if triplet > 0:
                triplet_words = process_triplet(triplet)
                if units[unit_index]:
                    triplet_words.append(units[unit_index])
                res.appendleft(" ".join(triplet_words))
            num //= 1000
            unit_index += 1

        return " ".join(res)
