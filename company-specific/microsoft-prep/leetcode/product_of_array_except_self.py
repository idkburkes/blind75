class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [1 for _ in range(n)]
        prod = 1
        
        for i in range(n):
            res[i] = prod
            prod *= nums[i]
            
        for i in range(n-2, -1, -1):
            res[i] = res[i] * nums[i+1]
            nums[i] = nums[i] * nums[i+1]
        
        return res
            
            