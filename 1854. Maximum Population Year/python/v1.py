from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        min_year = 1950
        max_year = 2050
        year_count = [0] * (max_year - min_year + 1)

        for birth, death in logs:
            for year in range(birth, death):
                year_count[year - min_year] += 1

        res_year = 1950
        max_population = 0

        for i, population in enumerate(year_count):
            if population > max_population:
                res_year = i + min_year
                max_population = population

        return res_year
