
## Dynamic Programming

Dynamic Programming is often used for OPTIMIZATION problems

We can use a top-down approach where we iteratively fill a matrix for solutions to subproblems and use those subproblems to solve the given question
Atlernatively, we can use MEMOIZATION where we store previously answered subproblems in a matrix/map to avoid solving subproblems more than once. Memoization solutions are usually recursive or utilize DFS.


- [X] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [X] [Coin Change](https://leetcode.com/problems/coin-change/)
- [ ] [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [ ] [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [ ] [Word Break Problem](https://leetcode.com/problems/word-break/)
- [X] [Combination Sum](https://leetcode.com/problems/combination-sum-iv/)
- [X] [House Robber](https://leetcode.com/problems/house-robber/)
- [ ] [House Robber II](https://leetcode.com/problems/house-robber-ii/)
- [ ] [Decode Ways](https://leetcode.com/problems/decode-ways/)
- [ ] [Unique Paths](https://leetcode.com/problems/unique-paths/)
- [X] [Jump Game](https://leetcode.com/problems/jump-game/)


Completed DP Problems not on Blind75

- [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)


List of all leetcode problems that follow knapsack pattern
[Leetcode Discussion](https://leetcode.com/discuss/study-guide/1200320/Thief-with-a-knapsack-a-series-of-crimes)


### How to approach most DP problems ###

Find recursive relation
- Recursive (top-down)
- Recursive + memo (top-down)
- Iterative + memo (bottom-up)
- Iterative + N variables (bottom-up)


Using House Robber example
Step 1. Figure out recursive relation.
A robber has 2 options: a) rob current house i; b) don't rob current house.
If an option "a" is selected it means she can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.
So it boils down to calculating what is more profitable:

robbery of current house + loot from houses before the previous
loot from the previous house robbery and any loot captured before that
rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )

Step 2. Recursive (top-down)
Converting the recurrent relation from Step 1 shound't be very hard.

```
public int rob(int[] nums) {
    return rob(nums, nums.length - 1);
}
private int rob(int[] nums, int i) {
    if (i < 0) {
        return 0;
    }
    return Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
}
```
This algorithm will process the same i multiple times and it needs improvement. Time complexity: [to fill]

Step 3. Recursive + memo (top-down).

```
    int[] memo;
public int rob(int[] nums) {
    memo = new int[nums.length + 1];
    Arrays.fill(memo, -1);
    return rob(nums, nums.length - 1);
}
```

```
private int rob(int[] nums, int i) {
    if (i < 0) {
        return 0;
    }
    if (memo[i] >= 0) {
        return memo[i];
    }
    int result = Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
    memo[i] = result;
    return result;
}
```

Much better, this should run in O(n) time. Space complexity is O(n) as well, because of the recursion stack, let's try to get rid of it.

Step 4. Iterative + memo (bottom-up)

```
    public int rob(int[] nums) {
    if (nums.length == 0) return 0;
    int[] memo = new int[nums.length + 1];
    memo[0] = 0;
    memo[1] = nums[0];
    for (int i = 1; i < nums.length; i++) {
        int val = nums[i];
        memo[i+1] = Math.max(memo[i], memo[i-1] + val);
    }
    return memo[nums.length];
}
```

Step 5. Iterative + 2 variables (bottom-up)
We can notice that in the previous step we use only memo[i] and memo[i-1], so going just 2 steps back. We can hold them in 2 variables instead. This optimization is met in Fibonacci sequence creation and some other problems [to paste links].

```
    /* the order is: prev2, prev1, num  */
public int rob(int[] nums) {
    if (nums.length == 0) return 0;
    int prev1 = 0;
    int prev2 = 0;
    for (int num : nums) {
        int tmp = prev1;
        prev1 = Math.max(prev2 + num, prev1);
        prev2 = tmp;
    }
    return prev1;
}
```

