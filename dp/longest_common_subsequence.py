# The solution for this problem uses bottom-up dp with 2D matrix
# We use the rows and columns to represent characters in each string
# We start with the LCS being zero at the bottom right of the matrix
# If the chars in a row and column of current grid match then the LCS
#   is 1 + the diagonal down+right. This is because when the chars match
#   then we move onto the next subproblem in the next row&column
#If the chars in a row and column of current grid don't match then the
#   LCS is the max of either the grid to the right or the grid down. This is 
#   because we have to continue search for the next subsequence that matches 
#   from these two options
#When the O(m*n) loop is complete, the answer will be in dp[0][0]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                down, right, diag = 0, 0, 0
                if i < m-1 and j < n-1: diag = dp[i+1][j+1]
                if i < m-1: down = dp[i+1][j]
                if j < n-1: right = dp[i][j+1]
                if text1[i] != text2[j]:
                    dp[i][j] = max(down, right)
                else:
                    dp[i][j] = diag + 1
        return dp[0][0]
                    
                
                
        
        
        