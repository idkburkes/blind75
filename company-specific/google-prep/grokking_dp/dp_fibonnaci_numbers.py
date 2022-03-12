

#######################################
# Fibonnaci Numbers
#######################################



# Problem Statement - Fibonnaci Number
# Write a function to calculate the nth Fibonacci number.

# Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers.
# First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …

# Mathematically we can define the Fibonacci numbers as:
#    Fib(n) = Fib(n-1) + Fib(n-2), for n > 1
#    Given that: Fib(0) = 0, and Fib(1) = 1

# This is DP solution with O(n) space. We can optimize this to O(1) space
def calculateFibonacci(n):
 
  dp = [0 for num in range(n+1)]
  dp[0] = 0
  dp[1] = 1

  for i in range(2,n + 1):
    dp[i] = dp[i-1] + dp[i-2]

  return dp[-1]

# We don't need to keep track of the entire DP array, we only really need to previous 2 numbers that have been calculated
# This is a great example of how we can optimize DP solutions for constant space.
def calculateFibonacciConstantSpace(n):
    if n < 2:
        return n

    # start with 2 initial fibonacci numbers for n = 0 and n = 1
    a, b, temp = 0, 1, 0

    for _ in range(2,n + 1):
        temp = a + b
        a = b
        b = temp
    # The nth fibonacci number will be stored in b after for loop finishes
    return b
  
# Problem Statement - Climbing Stairs
# Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.

# Example 1:
# Number of stairs (n) : 3
# Number of ways = 4
# Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3} 

# Example 2:
# Number of stairs (n) : 4
# Number of ways = 7
# Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1}, 
# {2,2}, {1,3}, {3,1}

# Here is the O(1) space solution. 
# It is the same as fibonacci numbers except we have to take the sum of the last 3 numbers rather than the last 2 numbers.
# This problem can be generalized to the last K numbers. In this case we'll have to keep track of all least that many numbers
# in a dp array so the space will be O(k) which is still better than O(n) in most cases
def count_ways(n):
  steps = {0:1, 1:1, 2:2}
  if n < 3:
    return steps[n]
  
  a = 1
  b = 1
  c = 2

  for _ in range(3,n+1):
    d = a + b + c
    a = b
    b = c
    c = d

  return c



# Problem Statement - Number factors
# Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.

# Example 1:
# n : 4
# Number of ways = 4
# Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3}, {3,1}, {4} 

# Example 2:
# n : 5
# Number of ways = 6
# Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1}, 
# {1,4}, {4,1}

# here is the fibonacci-esque solution with O(n) space and O(n) time. Since we have to save previous values beyond the last "k"
# it is required that we maintain an entire dp array so linear space is optimal.

def count_ways(n):
  
  dp = [0 for _ in range(n+1)]
  dp[0] = 1
  dp[1] = 1
  dp[2] = 1
  dp[3] = 2
  for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
  return dp[n]


# Problem Statement - Min Jumps (Jump Game 2)
# Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element,
# write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element).
# If an element is 0, then we cannot move through that element.

# Example 1:
# Input = {2,1,1,1,4}
# Output = 3
# Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4

# Example 2:
# Input = {1,1,3,6,9,3,0,1,3}
# Output = 4
# Explanation: Starting from index '0', we can reach the last index through: 0->1->2->3->8

# This is actually similar to a BFS approach. Each pass we'll figure out what is the max reachable in the current range.
# The initial state is the max reachable is whatever the first number is.
# We'll mark that as our last jump position then iterate the array up to that point, finding the max reachable within our range
# Once we reach our last jump position, we'll set the next jump position to whatever we found to be the max reachable 
# This is similar to a BFS 'level'
# We'll continue this process until the jump position is outside of the array, this means we can reach the end  
class Solution:
    def jump(self, nums: List[int]) -> int:
      n = len(nums)
      i = jumps = lastJumpPos = maxReachable = 0
      while lastJumpPos < n - 1:
        maxReachable = max(maxReachable, i + nums[i])
        if i == lastJumpPos:
          lastJumpPos = maxReachable
          jumps += 1
        i += 1
      
      return jumps
          


# Problem Statement - Minimum jumps with fee
# Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you take the step.
# Implement a method to calculate the minimum fee required to reach the top of the staircase (beyond the top-most step).
# At every step, you have an option to take either 1 step, 2 steps, or 3 steps. You should assume that you are standing at the first step.

# Example 1:
# Number of stairs (n) : 6
# Fee: {1,2,5,2,1,2}
# Output: 3
# Explanation: Starting from index '0', we can reach the top through: 0->3->top
# The total fee we have to pay will be (1+2).

# Example 2:
# Number of stairs (n): 4
# Fee: {2,3,4,5}
# Output: 5
# Explanation: Starting from index '0', we can reach the top through: 0->1->top
# The total fee we have to pay will be (2+3).
          
def find_min_fee(fee):
  n = len(fee)
  dp = [0 for x in range(n+1)]  # +1 to handle the 0th step
  dp[0] = 0  # if there are no steps, we don't have to pay any fee
  dp[1] = fee[0]  # only one step, so we have to pay its fee
  # for 2 steps, since we start from the first step, so we have to pay its fee
  # and from the first step we can reach the top by taking two steps, so
  # we don't have to pay any other fee.
  dp[2] = fee[0]

  # please note that dp[] has one extra element to handle the 0th step
  for i in range(2, n):
    dp[i + 1] = min(fee[i] + dp[i], 
                    fee[i - 1] + dp[i - 1], 
                    fee[i - 2] + dp[i - 2])

  return dp[n]

# Problem Statement - House Robber

# There are n houses built in a line. A thief wants to steal the maximum possible money from these houses.
# The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the security system.
# How should the thief maximize his stealing?

# Given a number array representing the wealth of n houses,
# determine the maximum amount of money the thief can steal without alerting the security system.

# Example 1:
# Input: {2, 5, 1, 3, 6, 2, 4}
# Output: 15
# Explanation: The thief should steal from houses 5 + 6 + 4

# Example 2:
# Input: {2, 10, 14, 8, 1}
# Output: 18
# Explanation: The thief should steal from houses 10 + 8

def find_max_steal(wealth):
  
  n = len(wealth)

  n1 = 0
  n2 = wealth[0]

  for i in range(1, n):
    temp = n1
    n1 = n2
    n2 = max(n1, wealth[i] + temp)

  return n2