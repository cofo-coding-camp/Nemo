class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        
        m = len(grid[0])
        n = len(grid)
        dp = [0] * m
        dp[0] = grid[0][0]

        for i in range(1, m):
                dp[i] = dp[i - 1] + grid[0][i]
        
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        
        return dp[-1]