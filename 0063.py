class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col == 0:
                    continue
                else:
                    dp[col] += dp[col - 1]
        return dp[-1]