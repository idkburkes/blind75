class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        index, n , triplets = 0, len(nums), []
        while index <= n -3:
            self.find_triplets(nums, triplets, index, -nums[index])
            index += 1
            while index < n and nums[index] == nums[index-1]: # skip duplicates
                index += 1
        return triplets
    
    def find_triplets(self, nums, triplets, index, target) -> None:
        left, right = index + 1, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                triplets.append([nums[index], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right: #skip duplicates
                    left += 1
            elif nums[left] + nums[right] < target:
                left += 1
                while nums[left] == nums[left - 1] and left < right: #skip duplicates
                    left += 1
            else:
                right -= 1
                while nums[right] == nums[right + 1] and left < right: #skip duplicates
                    right -= 1


