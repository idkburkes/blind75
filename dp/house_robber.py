

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

        

