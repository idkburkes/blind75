

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub('[^a-zA-Z0-9]', '', s).lower()
        start, end = 0, len(string)-1
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True
        