class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n)]
        return self.climb_recursive(n, dp)
        
        
    def climb_recursive(self, steps_remaining, dp):
        if steps_remaining == 0:
            return 1
           
        if dp[steps_remaining] == -1:
            one_step = self.climb_recursive(steps_remaining - 1)
            two_step = self.climb_recursive(steps_remaining - 2)
            dp[steps_remaining] = one_step + two_step
        
        return dp[steps_remaining]