#######################################
# Longest Palindromic Subsequence
#######################################


# Problem Statement - Longest Palindromic Subsequence

# Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
# In a palindromic subsequence, elements read the same backward and forward.
# A subsequence is a sequence that can be derived from another sequence by deleting some or
# no elements without changing the order of the remaining elements.

# Example 1:
# Input: "abdbca"
# Output: 5
# Explanation: LPS is "abdba".

# Example 2:
# Input: = "cddpd"
# Output: 3
# Explanation: LPS is "ddd".

# Example 3:
# Input: = "pqr"
# Output: 1
# Explanation: LPS could be "p", "q" or "r".

# The key here is that since its a subsequence (palindromes don't have to be adjacent/continuous)
# then we can just use a running sum of the max length at any point in the sequence. 
# If two chars are the same then the max length is 2 + whatever the max length is between those two chars

def find_LPS_length(st):
  n = len(st)
  # dp[i][j] stores the length of LPS from index 'i' to index 'j'
  dp = [[0 for _ in range(n)] for _ in range(n)]

  # every sequence with one element is a palindrome of length 1
  for i in range(n):
    dp[i][i] = 1

  for startIndex in range(n - 1, -1, -1):
    for endIndex in range(startIndex + 1, n):
      # case 1: elements at the beginning and the end are the same
      if st[startIndex] == st[endIndex]:
        dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
      else:  # case 2: skip one element either from the beginning or the end
        dp[startIndex][endIndex] = max(
          dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])

  return dp[0][n - 1]


# Problem Statement - Longest Common Substring
# Given a string, find the length of its Longest Palindromic Substring (LPS). 
# In a palindromic string, elements read the same backward and forward.

# Example 1:
# Input: "abdbca"
# Output: 3
# Explanation: LPS is "bdb".

# Example 2:
# Input: = "cddpd"
# Output: 3
# Explanation: LPS is "dpd".

# Example 3:
# Input: = "pqr"
# Output: 1
# Explanation: LPS could be "p", "q" or "r".

def find_LPS_length(st):
  n = len(st)
  # dp[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
  dp = [[False for _ in range(n)] for _ in range(n)]

  # every string with one character is a palindrome
  for i in range(n):
    dp[i][i] = True

  maxLength = 1
  for startIndex in range(n - 1, -1, -1):
    for endIndex in range(startIndex + 1, n):
      if st[startIndex] == st[endIndex]:
        # if it's a two character string or if the remaining string is a palindrome too
        if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
          dp[startIndex][endIndex] = True
          maxLength = max(maxLength, endIndex - startIndex + 1)

  return maxLength


# Problem Statement - Count of Palindromic Substrings
# Given a string, find the total number of palindromic substrings in it.
# Please note we need to find the total number of substrings and not subsequences.

# Example 1:
# Input: "abdbca"
# Output: 7
# Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".

# Example 2:
# Input: = "cddpd"
# Output: 7
# Explanation: Here are the palindromic substrings, "c", "d", "d", "p", "d", "dd", "dpd".

# Example 3:
# Input: = "pqr"
# Output: 3
# Explanation: Here are the palindromic substrings,"p", "q", "r".

# The solution here is the same as finding the longest palindromic substring except we count the total palindromes
# rather than keeping track of the substring itself
def count_PS(s):
 
  n = len(s)
  dp = [[False for col in range(n)] for row in range(n)]
  res = 0

  # Preprocess length 1 palindrome
  for i in range(n):
    dp[i][i] = True
    res += 1

  # Preprocess length 2 palindrome
  for i in range(i, n-1):
    if s[i] == s[i+1]:
      dp[i][i+1] = True
      res += 1

  for start in range(n-2, -1, -1):
    for end in range(start + 1, n):
      if s[start] == s[end] and dp[start+1][end-1]:
        dp[start][end] = True
        res += 1

  return res


# Problem Statement - Minimum deletions to make it a palindrome
# Given a string, find the minimum number of characters that we can remove to make it a palindrome.

# Example 1:
# Input: "abdbca"
# Output: 1
# Explanation: By removing "c", we get a palindrome "abdba".

# Example 2:
# Input: = "cddpd"
# Output: 2
# Explanation: Deleting "cp", we get a palindrome "ddd".

# Example 3:
# Input: = "pqr"
# Output: 2
# Explanation: We have to remove any two characters to get a palindrome, e.g. if we 
# remove "pq", we get palindrome "r".


# Solution
# This problem can be easily converted to the Longest Palindromic Subsequence (LPS) problem.
# We can use the fact that LPS is the best subsequence we can have, so any character that is not part of LPS must be removed.
# Please note that it is ‘Longest Palindromic SubSequence’ and not ‘Longest Palindrome Substring’.

# So, our solution for a given string ‘st’ will be:
# Minimum_deletions_to_make_palindrome = Length(st) - LPS(st)

def find_minimum_deletions(st):
  # subtracting the length of Longest Palindromic Subsequence from the length of
  # the input string to get minimum number of deletions
  return len(st) - find_LPS_length(st)


def find_LPS_length(st):
  n = len(st)
  # dp[i][j] stores the length of LPS from index 'i' to index 'j'
  dp = [[0 for _ in range(n)] for _ in range(n)]

  # every sequence with one element is a palindrome of length 1
  for i in range(n):
    dp[i][i] = 1

  for startIndex in range(n - 1, -1, -1):
    for endIndex in range(startIndex + 1, n):
      # case 1: elements at the beginning and the end are the same
      if st[startIndex] == st[endIndex]:
        dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
      else:  # case 2: skip one element either from the beginning or the end
        dp[startIndex][endIndex] = max(
          dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])

  return dp[0][n - 1]


##### SIMILAR PROBLEMS ###

# 1. Minimum insertions in a string to make it a palindrome
# Will the above approach work if we make insertions instead of deletions?
# Yes, the length of the Longest Palindromic Subsequence is the best palindromic subsequence we can have. 
# 
# Let’s take a few examples:
# Example 1:
# Input: "abdbca"   
# Output: 1  
# Explanation: By inserting “c”, we get a palindrome “acbdbca”.

# Example 2:
# Input: = "cddpd"  
# Output: 2  
# Explanation: Inserting “cp”, we get a palindrome “cdpdpdc”. We can also get a palindrome by inserting “dc”: “cddpddc”

# Example 3:
# Input: = "pqr"  
# Output: 2  
# Explanation: We have to insert any two characters to get a palindrome (e.g. if we insert “pq”, we get a palindrome “pqrqp”).


# 2. Find if a string is K-Palindromic#
# Any string will be called K-palindromic if it can be transformed into a palindrome by removing at most ‘K’ characters from it.
# This problem can easily be converted to our base problem of finding the minimum deletions in a string to make it a palindrome. 
# If the “minimum deletion count” is not more than ‘K’, the string will be K-Palindromic.




# Problem Statement - Palindromic Partitioning
# Given a string, we want to cut it into pieces such that each piece is a palindrome.
# Write a function to return the minimum number of cuts needed.

# Example 1:
# Input: "abdbca"
# Output: 3
# Explanation: Palindrome pieces are "a", "bdb", "c", "a".

# Example 2:
# Input: = "cddpd"
# Output: 2
# Explanation: Palindrome pieces are "c", "d", "dpd".

# Example 3:
# Input: = "pqr"
# Output: 2
# Explanation: Palindrome pieces are "p", "q", "r".

# Example 4:
# Input: = "pp"
# Output: 0
# Explanation: We do not need to cut, as "pp" is a palindrome.


# To solve this we first have to fill a 2D DP array identifying which substrings are palindromes
# This will be the same exact approach that we took in the Longest Palindromic Substring problem
# After we find out which substrings are palindromes then we can use DP again to figure out the 
# minimum cuts by iterating over every substring in a loop with O(n^2) time complexity. In each
# iteration starting from the end to beginning in reverse, we'll keep track of the minimum amount
# of palindromes that were found before each index. After completion the result will be in the first index
# with a count of the minimum amount of palindromes that were found in the entire string.
def find_MPP_cuts(st):
  n = len(st)
  # isPalindrome[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
  isPalindrome = [[False for _ in range(n)] for _ in range(n)]

  # every string with one character is a palindrome
  for i in range(n):
    isPalindrome[i][i] = True

  # populate isPalindrome table
  for startIndex in range(n-1, -1, -1):
    for endIndex in range(startIndex+1, n):
      if st[startIndex] == st[endIndex]:
        # if it's a two character string or if the remaining string is a palindrome too
        if endIndex - startIndex == 1 or isPalindrome[startIndex + 1][endIndex - 1]:
          isPalindrome[startIndex][endIndex] = True

  # now lets populate the second table, every index in 'cuts' stores the minimum cuts needed
  # for the substring from that index till the end
  cuts = [0 for _ in range(n)]
  for startIndex in range(n-1, -1, -1):
    minCuts = n  # maximum cuts
    for endIndex in range(n-1, startIndex-1, -1):
      if isPalindrome[startIndex][endIndex]:
        # we can cut here as we got a palindrome
        # also we don't need any cut if the whole substring is a palindrome
        minCuts = 0 if endIndex == n-1 else min(minCuts, 1 + cuts[endIndex + 1])

    cuts[startIndex] = minCuts

  return cuts[0]