class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_stack = list(word)
        abbr_stack = list(abbr)
        number_list = []

        while len(word_stack) != 0 or len(abbr_stack) != 0:
            if len(word_stack) == 0:
                return False
            if len(abbr_stack) == 0:
                return False

            current_char = abbr_stack.pop(0)

            if current_char.isdigit():
                if current_char == "0" and len(number_list) == 0:
                    return False
                number_list.append(current_char)
                if len(abbr_stack) == 0:
                    concatenated_string = "".join(number_list)
                    skip_count = int(concatenated_string)
                    return skip_count == len(word_stack)
            else:
                if len(number_list) != 0:
                    concatenated_string = "".join(number_list)
                    skip_count = int(concatenated_string)
                    if skip_count > len(word_stack) - 1:
                        return False
                    for _ in range(skip_count):
                        word_stack.pop(0)
                    number_list = []

                if word_stack.pop(0) != current_char:
                    return False

        return True
