# Solution 1 - DP O(n^2)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if not n:
            return 0
        
        dp = [[0] * i for i in range(1, n+1)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for k in range(i + 1):
                if k == 0:
                    dp[i][k] = dp[i-1][k] + triangle[i][k]
                elif k == i:
                    dp[i][k] = dp[i-1][k-1] + triangle[i][k]
                else:
                    dp[i][k] = min(dp[i-1][k-1], dp[i-1][k]) + triangle[i][k]
        return min(dp[-1])

# Solution 2 - DP O(n)
# TODO:debug


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n
        for i in range(len(triangle[-1])):
            dp[i] = triangle[-1][i]
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

# Solution 3 - DFS with Cache


import functools
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @functools.lru_cache(None)
        def DFS(level, i, j):
            if level == n:
                return 0
            res = 0
            a = float('inf')
            b = float('inf')
            if 0 <= i < len(triangle[level]):
                a = DFS(level+1, i, i+1) + triangle[level][j]
            if 0 <= j < len(triangle[level]):
                b = DFS(level+1, j, j+1) +triangle[level][j]
            res += min(a, b)
            return res

        return DFS(0, -1, 0)