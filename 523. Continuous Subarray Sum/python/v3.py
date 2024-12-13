from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        state_to_first_seen = {0: -1}
        state = 0
        for i, num in enumerate(nums):
            state = (state + num) % k
            if state in state_to_first_seen:
                if i - state_to_first_seen[state] > 1:
                    return True
            else:
                state_to_first_seen[state] = i

        return False
