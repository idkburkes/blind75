


## String

- [X] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [X] [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [X] [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [X] [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [ ] [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [X] [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [X] [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [X] [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [ ] [Encode and Decode Strings (Leetcode Premium)](https://leetcode.com/problems/encode-and-decode-strings/)

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