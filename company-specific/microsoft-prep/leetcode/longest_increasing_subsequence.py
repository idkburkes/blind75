class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
                    res = max(dp[i], res)
                    
        return res
        