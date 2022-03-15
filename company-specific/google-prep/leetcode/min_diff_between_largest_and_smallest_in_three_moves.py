
# You are given an integer array nums. In one move, you can choose one element of nums and change it by any value.
# Return the minimum difference between the largest and smallest value of nums after performing at most three moves.


# Very good solution on discussions -> https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/731233/Similar-to-1423.-Maximum-Points-You-Can-Obtain-from-Cards

# O(nlogn) time with a sorted array, we'll create a sliding window excluding 3 values at all times, starting with the last 3 values
# Since the array is sorted we can find the min difference by taking the difference between the first and last numbers currently in the window
# Keep track of the absolute minimum throughout this entire linear traversal.

def minDifference(self, nums: List[int]) -> int:
    
    nums = sorted(nums)
    n = len(nums)
    if n <= 3: 
        return 0
    
    i = 0
    # this can be generalized to n - k - 1 for other problems
    j = n - 4
    minDif = float('inf')
    
    while j < n:
        minDif = min(minDif, nums[j] - nums[i])
        i += 1
        j += 1
    return minDif