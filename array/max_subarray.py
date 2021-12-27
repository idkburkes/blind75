

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums or n == 0:
            return 0
        elif n == 1:
            return nums[0]
        #This is Kadane's Algorithm
        max_sum, current = nums[0], nums[0]
        for i in range(1,n):
            current = max(nums[i], current + nums[i])
            if current > max_sum: 
                max_sum = current
        return max_sum        



            

        