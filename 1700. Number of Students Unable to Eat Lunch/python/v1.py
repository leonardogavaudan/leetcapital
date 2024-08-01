from typing import Counter, List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preference_to_count = Counter(students)
        sandwich_index = 0
        students_unfed_count = len(students)

        while students_unfed_count != 0:
            if preference_to_count[sandwiches[sandwich_index]] == 0:
                return students_unfed_count
            else:
                preference_to_count[sandwiches[sandwich_index]] -= 1
                sandwich_index += 1
                students_unfed_count -= 1

        return 0
