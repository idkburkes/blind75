

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for col in range(target+1)]
        nums = sorted(nums)

        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                elif num == i:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-num]
        return dp[target]





        