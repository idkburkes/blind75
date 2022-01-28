
# This solution uses built in functions. Lets try to do this in place in O(n) time and O(1) space
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        
        words = s.split()
        i, j = 0, len(words) - 1
        while i < j:
            temp = words[i].strip()
            words[i] = words[j].strip()
            words[j] = temp
            i, j = i + 1, j - 1
        return ''.join(words)

    



        