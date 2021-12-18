

# https://leetcode.com/problems/partition-equal-subset-sum/
# Bottom-up DP solution for a problem that is similar to Knapsack 0/1


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       s = sum(nums)
       if s%2:
          return False
       n = len(nums)
       if n <= 1:
         return False
       target = s//2
       dp = [[False for sumcol in range(target + 1)] for num in range(n)] # dp[num][sum]
       # preprocess null sets as True
       for num in range(n):
          dp[num][0] = True
       # preprocess sum = first item as true
       if nums[0] <= target:
         dp[0][nums[0]] = True 
       # fill matrix of size (n * sum)
       for i in range(1,n):
         for j in range(1,target + 1):
           if j - nums[i] >= 0:
             dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]]
           else:
             dp[i][j] = dp[i-1][j]
             

       return dp[n-1][target] #bottom right grid contains answer