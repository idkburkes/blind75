class Solution:

    # Not pretty but you get the idea 
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False
        elif len(s) != len(t):
            return False
        s_dict = {}
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        for letter in t:
            if letter not in s_dict:
                return False
            else:
                s_dict[letter] = s_dict.get(letter) - 1
                if s_dict[letter] == 0:
                    del s_dict[letter]
            
        return len(s_dict) == 0
            
        