
class Solution:
        def wordBreakBottomUp(self, s: str, wordDict: List[str]) -> bool:
            dp = [False] * (len(s) + 1)
            dp[len(s)] = True

            for i in range(len(s) + 1, -1, -1):
                for w in wordDict:
                    if len(w) + i <= len(s) and s[i : i + len(w)] == w:
                        dp[i] = dp[i + len(w)]
                    if dp[i]:
                        break
            return dp[0]
                
    # this recursive solution is not optimal or pass all test cases. 
    # But does give a little intution about how the problem is solved w recurrence relation
        def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            memo = [[-1 for col in range(len(s))] for row in range(len(s))]
            return self.break_recursive(s, wordDict, 0, 1, memo)


        def break_recursive(self, s, wordDict, start, end, memo):
            n = len(s)
            if ''.join(s[start:n]) in wordDict:
                return True
            if end >= n:
                return False
        
            if memo[start][end] != -1:
                return memo[start][end] == 1

            include, exclude = False, False
            if ''.join(s[start:end]) in wordDict:
                include = self.break_recursive(s, wordDict, end, end+1, memo)
            else:
                exclude = self.break_recursive(s, wordDict, start, end+1, memo)
        
            memo[start][end] = 1 if (include or exclude) else 0
            return memo[start][end] == 1



