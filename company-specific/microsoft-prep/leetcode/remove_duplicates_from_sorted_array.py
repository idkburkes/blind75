class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        write = 0
        while i < n:
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            nums[write] = nums[i]
            write += 1
            i += 1
        
        return write
        
            
            
        