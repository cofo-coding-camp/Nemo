class Solution:
    def calculate(self, s: str) -> int:
        signs = []
        num = 0
        res = 0
        sign = 1
        for foo in s:
            if foo.isdigit():
                num = num * 10 + int(foo)
            elif foo == '(':
                signs.append(sign)
            elif foo == ')':
                signs.pop()
            elif foo in('-', '+'):
                res += num * sign
                num = 0
                op = 1
                if signs:
                    op = signs[-1]
                sign = op * (1 if foo == '+' else -1)
        return res + sign * num
