class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            res[i] =  prod
            prod *= nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i] * nums[i+1]
            nums[i] = nums[i] * nums[i+1]
            
        return res
            
        
        
            