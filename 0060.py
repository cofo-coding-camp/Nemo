from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if not n:
            return []
        nums = [i for i in range(1, n + 1)]
        used = [False] * n

        def backtrack(depth, pre):
            nonlocal n, k
            if depth == n:
                return ''.join(pre)

            ps = factorial(n - 1 - depth)
            for i in range(n):
                if used[i]:
                    continue
                if ps < k:
                    k -= ps
                    continue
                pre.append(str(nums[i]))
                used[i] = True
                return backtrack(depth + 1, pre)

        return backtrack(0, [])
