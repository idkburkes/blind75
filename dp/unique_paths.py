class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [[-1 for j in range(n)] for i in range(m)]
        return self.path_recursive(self, m, n, 0, 0, memo)

    def path_recursive(self, m, n, row, col, memo):
        if row > m-1 or col > n-1:
            return 0

        if row == m-1 and col == n-1:
            return 1

        if memo[row][col] != -1:
            return memo[row][col]
        
        right = self.path_recursive(m, n, row, col+1, memo)
        down = self.path_recursive(m, n, row+1, col, memo)
        
        memo[row][col] = right + down
        return right + down



    def uniquePathsIterative(self, m: int, n: int) -> int:
        dp = [[0 for col in range(n)] for row in range(m)]

        for i in range(m):
            dp[m][0] = 1
        for i in range(n):
            dp[0][n] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]

    

        