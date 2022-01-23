class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        dp = [0 for _ in range(n)]
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[i] = 1
            else:
                break
        
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                    dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j] + dp[j-1]
        return dp[-1]