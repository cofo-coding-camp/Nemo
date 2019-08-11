class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        l = len(A)
        total = sum(A)
        if not l:
            return 0
        f = sum([i * A[i] for i in range(l)])
        res = f
        for i in range(l - 1, -1, -1):
            f += total - l * A[i]
            res = max(res, f)
        return res