from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = sorted(people)
        i, j = 0, len(people) - 1
        res = 0

        while i <= j:
            if sorted_people[i] + sorted_people[j] <= limit:
                i += 1

            j -= 1
            res += 1

        return res
