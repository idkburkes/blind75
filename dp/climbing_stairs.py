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


    # This climbing stairs problem is essentially the fibonacci sequence
    # We can solve iteratively using bottom-up starting from the beginning
    # of 1D dp array
    def climbStairsIterative(self, n: int) -> int:
        if n == 1: return 1
        dp = [0 for i in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

    # We can also use O(1) space remembering that to solve this sequence
    # We only need to previous 2 numbers. We don't have to keep track of the entire
    # DP array! This translates to more complicated dp problems where we only
    # need to keep track of the previous row.
    def climbStairsIterativeConstantSpace(self, n:int) -> int:
        if n == 1:
             return 1
        elif n == 2:
             return 2
        a, b = 1, 2
        for _ in range(2,n-1):
            c = a + b
            a = b
            b = c
        return a + b