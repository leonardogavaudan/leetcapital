class Solution:
    def pivotInteger(self, n: int) -> int:
        a = 2
        b = 0
        c = -n * (n + 1)

        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            return -1

        solution = (-b + discriminant**0.5) / (2 * a)

        return int(solution) if solution > 0 and solution % 1 == 0 else -1
