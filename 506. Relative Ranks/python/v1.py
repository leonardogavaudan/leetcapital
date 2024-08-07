from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, key=lambda x: -x)
        score_to_relative_rank = {}
        for i, s in enumerate(sorted_scores):
            score_to_relative_rank[s] = i + 1

        answer = []

        for s in score:
            if score_to_relative_rank[s] == 1:
                answer.append("Gold Medal")
            elif score_to_relative_rank[s] == 2:
                answer.append("Silver Medal")
            elif score_to_relative_rank[s] == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(f"{score_to_relative_rank[s]}")

        return answer
