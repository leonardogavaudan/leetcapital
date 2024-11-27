class Solution:
    def process(self, num: int):
        if num == 0:
            return []

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

        res = []

        hundred = num // 100
        if hundred:
            res.extend([digit_to_regular[hundred], "Hundred"])

        digit_to_partial_ten = {
            2: "Twen",
            3: "Thir",
            4: "For",
            5: "Fif",
            6: "Six",
            7: "Seven",
            8: "Eigh",
            9: "Nine",
        }
        digit_to_partial_teen = {
            3: "Thir",
            4: "Four",
            5: "Fif",
            6: "Six",
            7: "Seven",
            8: "Eigh",
            9: "Nine",
        }

        ten_and_one = num % 100
        if ten_and_one == 10:
            res.append("Ten")
        elif ten_and_one == 11:
            res.append("Eleven")
        elif ten_and_one == 12:
            res.append("Twelve")
        elif ten_and_one in range(13, 20):
            res.append(digit_to_partial_teen[ten_and_one % 10] + "teen")
        else:
            ten = (num % 100) // 10
            if ten:
                res.append(digit_to_partial_ten[ten] + "ty")
            one = ten_and_one % 10
            if one:
                res.append(digit_to_regular[one])

        return res

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        units = [[], ["Thousand"], ["Million"], ["Billion"]]
        unit_i = 0
        res = []
        while num:
            processed = self.process(num % 1000)
            if processed:
                res = processed + units[unit_i] + res
            num //= 1000
            unit_i += 1

        return " ".join(res)
