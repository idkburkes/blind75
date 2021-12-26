
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in dict:
                return [dict.get(target-nums[i]), i]
            else:
                dict[nums[i]] = i
          