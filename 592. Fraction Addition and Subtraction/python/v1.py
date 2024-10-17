class Solution:
    def fractionAddition(self, expression: str) -> str:
        i = 0
        prev = 0

        def get_next():
            nonlocal i, prev

            while expression[i] != "/":
                i += 1

            num = int(expression[prev:i])
            i += 1
            prev = i

            while i < len(expression) and expression[i] not in ["+", "-"]:
                i += 1

            denum = int(expression[prev:i])
            prev = i

            return (num, denum)

        def get_hca(x: int, y: int) -> int:
            while y:
                x, y = y, x % y
            return x

        num, denum = get_next()

        lca = get_hca(abs(num), denum)
        num //= lca
        denum //= lca

        while i < len(expression):
            new_num, new_denum = get_next()
            num = new_denum * num + denum * new_num
            denum = denum * new_denum

            lca = get_hca(abs(num), denum)
            if lca:
                num //= lca
                denum //= lca

        if num == 0:
            return "0/1"

        return f"{num}/{denum}"
