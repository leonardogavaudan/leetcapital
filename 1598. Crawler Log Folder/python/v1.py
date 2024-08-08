from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current_dir = "./"
        parent_dir = "../"

        depth = 0

        for log in logs:
            if log == current_dir:
                continue
            if log == parent_dir:
                depth = max(0, depth - 1)
            else:
                depth += 1

        return depth
