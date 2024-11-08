class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        res = float("inf")
        seen = set()

        def recurse(A_count: int, copy_count: int, operations_count: int):
            nonlocal n, res, seen
            if (A_count, copy_count, operations_count) in seen:
                return
            if A_count > n:
                seen.add((A_count, copy_count, operations_count))
                return
            if A_count == n:
                res = min(res, operations_count)
                seen.add((A_count, copy_count, operations_count))
                return

            # copy + paste
            recurse(A_count * 2, A_count, operations_count + 2)
            # paste
            recurse(A_count + copy_count, copy_count, operations_count + 1)

        recurse(1, 1, 1)

        return int(res)
