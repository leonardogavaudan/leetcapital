from typing import List

class Solution:
    def __init__():
        self.char_to_index = {} 

    def compare(self, str1: str, str2: str) -> int:
        i = 0

        while i < len(str1) and i < len(str2):
            if self.char_to_index[str1[i]] < self.char_to_index[str2[i]]:
                return -1
            elif self.char_to_index[str1[i]] > self.char_to_index[str2[i]]:
                return 1

            i += 1

        if len(str1) < len(str2):
            return -1
        elif len(str1) > len(str2):
            return 1
        else:
            return 0

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i, c in enumerate(order):
            self.char_to_index[c] = i

        for i in range(len(words) - 1):
            comparison = self.compare(words[i], words[i + 1])
            if comparison == 1:
                return False
            
        return True
