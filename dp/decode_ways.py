class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '' or s is None:
            return 0
        dp = [0 for num in range(len(s)+1)]
        dp[0] = 1

        for i in range(1,len(s)+1):
            #single
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            #double
            if i != 1 and s[i-2:i] < '27' and s[i-2:i] > '09':
                dp[i] += dp[i-2]
        return dp[len(s)]  