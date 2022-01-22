class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1,1
        res = nums[0]
        
        for num in nums:
            vals = (num, num * curMax, num * curMin)
            curMax, curMin = max(vals), min(vals)
            res = max(curMax, res)
        
        return res
        