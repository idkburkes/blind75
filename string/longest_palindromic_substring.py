class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if s is None or n == 0:
            return ''
        elif n == 1:
            return s[0]
        elif n == 2:
            return s if s[0] == s[1] else s[0]
        elif len(set(s)) == 1:
            return s
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = s[0]
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res = s[i:i+2]
                
        for k in range(3, n+1):
            for i in range(n-k+1):
                end = i+k-1
                if s[i] == s[end] and dp[i+1][end-1] == True:
                    dp[i][end] = True
                    res = s[i:end+1]
        
        return res
        