

class Solution:
    def rob(self, nums: List[int]) -> int:
        n  = len(nums)
        dp = [-1 for i in range(n)]
        return self.rob_recursive(nums, n-1)
    
    def rob_recursive(self, nums, index, dp):
        if index < 0:
            return 0

        if dp[index] > -1:
            return dp[index]
        
        include = nums[index] + self.rob_recursive(nums, index - 2, dp)
        exclude = self.rob_recursive(nums, index-1, dp)
        dp[index] = max(include, exclude)

        return dp[index]

    def robIterative(self, nums: List[int]) -> int:
        N = len(nums)
        if nums is None or N == 0:
            return 0
        elif N == 1:
            return nums[0]
        
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
         
        for i in range(2,N):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[N-1]


    def robIterativeSpaceOptimized(self, nums: List[int]) -> int:
        N = len(nums)
        if nums is None or N == 0:
            return 0
        elif N == 1:
            return nums[0]
        
        dp = [0] * N
        a = nums[0]
        b = max(nums[0],nums[1])
            
        for i in range(2,N):
            c = max(b, nums[i]+a)
            a = b
            b = c
                
        return b

        

