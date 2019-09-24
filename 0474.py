from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for item in strs:
            cache = Counter(item)
            for i in range(m, cache['0'] - 1, -1):
                for j in range(n, cache['1'] - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - cache['0']][j - cache['1']])
        
        return dp[m][n]