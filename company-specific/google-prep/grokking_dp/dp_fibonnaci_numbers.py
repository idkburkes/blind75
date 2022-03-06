

#######################################
# Fibonnaci Numbers
#######################################



# Problem Statement
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
    