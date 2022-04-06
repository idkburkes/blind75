class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        i = 0
        triplets = []
        
        while i < len(nums):
            self.find_triplets(nums, i, triplets, -nums[i])
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]: #skip duplicates
                i += 1
        
        return triplets
    
    
    def find_triplets(self, nums, i, triplets, target):
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] == target:
                triplets.append([nums[left], nums[right], nums[i]])
                left += 1
                # skip duplicates
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif nums[left] + nums[right] < target:
                left += 1
                # skip duplicates
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            else:
                right -= 1
                # skip duplicates
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
        