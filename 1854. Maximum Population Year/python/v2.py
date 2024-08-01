from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        start_year = 1950
        end_year = 2050
        year_count = [0] * (end_year - start_year + 1)

        for birth_year, death_year in logs:
            year_count[birth_year - start_year] += 1
            year_count[death_year - start_year] -= 1

        max_population = 0
        max_year = 0

        current_population = 0

        for i, pop_change in enumerate(year_count):
            current_population += pop_change
            if current_population > max_population:
                max_population = current_population
                max_year = i + start_year

        return max_year
