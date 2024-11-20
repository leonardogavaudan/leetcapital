from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        state = 0
        state_to_first_seen = {0: -1}

        for i, num in enumerate(nums):
            state = (state + num) % k
            if state in state_to_first_seen:
                if i - state_to_first_seen[state] >= 2:
                    return True
            else:
                state_to_first_seen[state] = i

        return False
