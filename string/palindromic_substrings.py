class Solution:
    def countSubstrings(self, s: str) -> int:
        res, n = 0, len(s)
        if s is None or n == 0:
            return 0
        elif n == 1:
            return 1
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        # All single chars are palindromes
        for i in range(n):
            dp[i][i] = True
            res += 1
            
        # Length 2 strings are palindromes if chars are the same
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res +=1 
        
        for k in range(3, n+1):
            for i in range(0,n-k+1):
                end = i+k-1
                if s[i] == s[end] and dp[i+1][end-1] == True:
                    dp[i][end] = True
                    res += 1          
        return res
        