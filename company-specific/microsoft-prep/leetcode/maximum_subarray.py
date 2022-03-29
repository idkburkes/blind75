def maxSubArray(self, nums: List[int]) -> int:
    maxsum = cursum = nums[0]
    
    for i in range(1, len(nums)):
        cursum = max(nums[i], cursum + nums[i])
        maxsum = max(maxsum, cursum)
        
    return maxsum