#######################################
# Longest Common Substring
#######################################
#
# Problem Statement - Longest Common Substring
# Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.
#--------------------
# Example 1:
# Input: s1 = "abdca"
#      s2 = "cbda"
# Output: 2
# Explanation: The longest common substring is "bd".
#-------------------
# Example 2:
# Input: s1 = "passport"
#       s2 = "ppsspt"
# Output: 3
# Explanation: The longest common substring is "ssp".

def find_LCS_length(s1, s2):
  m = len(s1)
  n = len(s2)
  res = 1
  dp = [[0 for col in range(n)] for row in range(m)]

  # populate first col
  for i in range(m):
    if s1[i] == s2[0]:
      dp[i][0] = 1
      res = 1
  # populate first row
  for i in range(n):
    if s1[0] == s2[i]:
      dp[0][i] = 1
      res = 1
# An alternative to prepopulating the first row & column is to add
# an extra row and column full of zeros, this way we could start on row 1 column 1 without
# ArrayOutOfBounds exceptionds
#
# After gaining more experience I have found that I prefer to use the extra row & column. See next question

  for i in range(1,m):
    for j in range(1,n):
      # If two letters are the same then the current length of common substring is 1 + the
      # length from the previous letter in both words   
      if s1[i] == s2[j]:
        dp[i][j] = dp[i-1][j-1] + 1
        res = max(res, dp[i][j])
  return res

 

# Problem Statement - Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.
#
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements 
# without changing the order of the remaining elements.
#
# Example 1:
# Input: s1 = "abdca"
#      s2 = "cbda"
# Output: 3
# Explanation: The longest common subsequence is "bda".
#
# Example 2:
# Input: s1 = "passport"
#      s2 = "ppsspt"
# Output: 5
# Explanation: The longest common subsequence is "psspt".
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
    m = len(text1)
    n = len(text2)
    dp = [[0 for col in range(n+1)] for row in range(m+1)]
    res = 0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            res = max(res, dp[i][j])
        
    return res



# Problem Statement - Minimum Deletions & Insertions to Transform a String into another
# Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters.
# Write a function to calculate the count of the minimum number of deletion and insertion operations.

# Example 1:
# Input: s1 = "abc"
#      s2 = "fbc"
# Output: 1 deletion and 1 insertion.
# Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.

# Example 2:
# Input: s1 = "abdca"
#      s2 = "cbda"
# Output: 2 deletions and 1 insertion.
# Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.

# Example 3:
# Input: s1 = "passport"
#       s2 = "ppsspt"
# Output: 3 deletions and 1 insertion
# Explanation: We need to delete {'a', 'o', 'r'} and insert {'p'} to s1 to transform it into s2.

# THE SOLUTION PATTERN FOR MINIMUM DELETIONS & INSERTIONS
# Seeing this type of question, it is a huge indicator that we'll need to use the longest subsequence or subsequence then
# subtract it from some known value (like the length of the string). This has shown up multiple times and it has stumped
# me now and a few times in the past. Learn this!!!

# Solution
# This problem can easily be converted to the Longest Common Subsequence (LCS).
# If we can find the LCS of the two input strings, we can easily find how many characters we need to insert and delete from s1.
# Here is how we can do this:

# 1. Let’s assume len1 is the length of s1 and len2 is the length of s2.
# 2. Now let’s assume c1 is the length of LCS of the two strings s1 and s2.
# 3. To transform s1 into s2, we need to delete everything from s1 which is not part of LCS, 
#           so minimum deletions we need to perform from s1 => len1 - c1
# 4. Similarly, we need to insert everything in s1 which is present in s2 but not part of LCS,
#           so minimum insertions we need to perform in s1 => len2 - c1
def find_MDI(s1, s2):
  c1 = find_LCS_length(s1, s2)
  print("Minimum deletions needed: " + str(len(s1) - c1))
  print("Minimum insertions needed: " + str(len(s2) - c1))


def find_LCS_length(s1,  s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
  maxLength = 0
  for i in range(1, n1+1):
    for j in range(1, n2+1):
      if s1[i - 1] == s2[j - 1]:
        dp[i][j] = 1 + dp[i - 1][j - 1]
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

      maxLength = max(maxLength, dp[i][j])

  return maxLength

# Problem Statement - Longest Increasing Subsequence
# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS).
# In an increasing subsequence, all the elements are in increasing order (from lowest to highest).
#
# Example 1:
# Input: {4,2,3,6,10,1,12}
# Output: 5
# Explanation: The LIS is {2,3,6,10,12}.
#
# Example 2:
# Input: {-4,10,3,7,15}
# Output: 4
# Explanation: The LIS is {-4,3,7,15}.
#
# This is a classic DP question that I should know how to do off the dome.
# Its a 1D dp problem with O(n^2) time

# 1. If the number at the current index is bigger than the number at the previous index, 
#              we increment the count for LIS up to the current index.
# 2. But if there is a bigger LIS without including the number at the current index, we take that.
#
# So we need to find all the increasing subsequences for the number at index ‘i’, 
# from all the previous numbers (i.e. number till index ‘i-1’), to eventually find the longest increasing subsequence.

def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    res = 1
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                res = max(res, dp[i])
    return res

# Problem Statement - Maximum Sum Increasing Subsequence
# Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.
#
# Example 1:
# Input: {4,1,2,6,10,1,12}
# Output: 32
# Explanation: The increaseing sequence is {4,6,10,12}. 
# Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.
#
# Example 2:
# Input: {-4,10,3,7,15}
# Output: 25
# Explanation: The increaseing sequences are {10, 15} and {3,7,15}.

# Pretty similar to maximum increasing subsequence, but instead of checking if the current dp length + 1 is greater than
# the longest length, we check if the current dp sum + the ith number is greater than the sum at dp[i] 
def find_MSIS(nums):
      n = len(nums)
      dp = [0] * n
      dp[0] = nums[0]
      res = nums[0]

      for i in range(1,n):
        dp[i] = nums[i]
        for j in range(i):
          if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
            dp[i] = dp[j] + nums[i]
          res = max(res, dp[i])

      return res


# Problem Statement - Shortest Common Supersequence 
# Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.

# Example 1:
# Input: s1: "abcf" s2:"bdcf" 
# Output: 5
# Explanation: The shortest common super-sequence (SCS) is "abdcf". 
#
# Example 2:
# Input: s1: "dynamic" s2:"programming" 
# Output: 15
# Explanation: The SCS is "dynprogrammicng". 

# The solution here is to realize that the length of the longest common subsequence + count of chars from string1 not contained
# in LCS + count of chars from string2 not contained in LCS is the length of the shortest common subsequence
def find_SCS_length(s1, s2):
  
  m = len(s1)
  n = len(s2)
  dp = [[0 for col in range(n+1)] for row in range(m+1)]

  # Find the longest common subsequence
  # we've already done this in a previous problem
  for i in range(1,m+1):
    for j in range(1,n+1):
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      if s1[i-1] == s2[j-1]:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

  # longest common subsequence
  lcs = dp[m][n]
  # chars in string1 that weren't in LCS
  remaining1 = m - lcs
  # chars in string2 that weren't in LCS
  remaining2 = n - lcs

  # sum all of these to get the shortest common super-sequence
  return lcs + remaining1 + remaining2

# Problem Statement - Minimum Deletions to make a sequence sorted 
# Given a number sequence, find the minimum number of elements that should be deleted to make the remaining sequence sorted.

# Example 1:
# Input: {4,2,3,6,10,1,12}
# Output: 2
# Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.

# Example 2:
# Input: {-4,10,3,7,15}
# Output: 1
# Explanation: We need to delete {10} to make the remaing sequence sorted {-4,3,7,15}.

# Example 3:
# Input: {3,2,1,0}
# Output: 3
# Explanation: Since the elements are in reverse order, we have to delete all except one to get a 
# sorted sequence. Sorted sequences are {3}, {2}, {1}, and {0}

# I had problems recalling the longest increasing subsequence pattern from memory. Practice this a few times.
def find_minimum_deletions(nums):
  n = len(nums)
  dp = [1] * n
  dp[0] = 1
  # Longest increasing subsequence
  LIS = 1
  for i in range(1,n):
    for j in range(i):
      if nums[i] > nums[j] and dp[i] <= dp[j]:
        dp[i] = dp[j] + 1
        LIS = max(LIS, dp[i])

  # Minimum deletions is difference between length of array and LIS
  min_dels = n - LIS
  return min_dels


# Problem Statement - Longest Repeating Subsequence
# Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).

# Example 1:
# Input: “t o m o r r o w”
# Output: 2
# Explanation: The longest repeating subsequence is “or” {tomorrow}.
#
# Example 2:
# Input: “a a b d b c e c”
# Output: 3
# Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.
#
# Example 3:
# Input: “f m f f”
# Output: 2
# Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}. Please note the second last character is shared in LRS.
#
# The problem is quite similar to the Longest Common Subsequence (LCS), with two differences:
# In LCS, we were trying to find the longest common subsequence between the two strings, whereas in LRS we are trying to find the two longest common subsequences within one string.
# In LRS, every corresponding character in the subsequences should not have the same index.
#
# If the two indexes are not the same and the characters at both the indexes are same, we can recursively match for the remaining length (i.e. by incrementing both the indexes).
# If the characters at both the indexes don’t match, we start two new recursive calls by incrementing each index separately. The LRS would be the one with the highest length from the two recursive calls.
#
# I think for this problem it would be helpful to take a look at the top-down approach with memoization for some intuition
def find_LRS_length(str):
  n = len(str)
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  return find_LRS_length_recursive(dp, str, 0, 0)


def find_LRS_length_recursive(dp,  str, i1, i2):
  n = len(str)
  if i1 == n or i2 == n:
    return 0

  if dp[i1][i2] == -1:
    if i1 != i2 and str[i1] == str[i2]:
      dp[i1][i2] = 1 + find_LRS_length_recursive(dp, str, i1 + 1, i2 + 1)
    else:
      c1 = find_LRS_length_recursive(dp, str, i1, i2 + 1)
      c2 = find_LRS_length_recursive(dp, str, i1 + 1, i2)
      dp[i1][i2] = max(c1, c2)

  return dp[i1][i2]

# Here is the bottom-up solution with O(n^2)
def find_LRS_length(s):
  n = len(s)
  dp = [[0 for col in range(n+1)] for row in range(n+1)]
  LRS = 0
  for i in range(1,n+1):
    for j in range(1,n+1):
      if s[i-1] == s[j-1] and i != j:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      LRS = max(LRS, dp[i][j])

  return LRS