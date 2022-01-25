## String

- [X] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [X] [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [X] [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [X] [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [X] [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [X] [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [X] [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [X] [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [ ] [Encode and Decode Strings (Leetcode Premium)](https://leetcode.com/problems/encode-and-decode-strings/)


--- 

### Group Anagrams ###
You can use tuples as a key to a dictionary! This is helpful for anagram problems. Also make note of the line where I use '+' operator to add a new value to list

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            key = tuple(sorted(word))
            res[key] = res.get(key, []) + [word]
        return list(res.values())


```

### Palindromic Substrings ###
I've got solution to palindromic substring problems that are currently O(N^2) time and space. I will have to do some research in the future to optimize these


### Valid Parentheses ###
My approach to solve this problem is to use a stack and iterate over the string once. Each time I encounter an open bracket I will push it to the stack. Each time I encounter a closed bracket, I will pop the first value of the stack and use a dictionary to compare it to the expected opening bracket for the closed bracket I encountered. If they don't match, or this is nothing on the stack then we'll return false. Finally, we will check to see if the stack has any remaining items. If it does then we know the brackets are not balanced because there were more opening brackets than closing brackets 
```python
    def isValid(self, s: str) -> bool:
        if s is None or not len(s): return True
        open_paren, stack = ('(','[','{'), []
        paren_map = {'}':'{',']':'[',')':'('}
        
        for c in s:
            if c in open_paren:
                stack.append(c)
            elif not stack or (stack.pop() != paren_map[c]):
                return False
            
        return not stack
```