from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        start = res = 0
        
        # Window end increments each iteration
        for end in range(len(s)):
            # Keep track of freq of each char in current window
            # Also keep track of which char is the most common
            counts[s[end]] += 1
            most_common = counts.most_common(1)[0][1]
            
            # If current window has more chars that aren't the most common
            # then move start index of window a decrement freq of chars leaving
            while (end - start + 1) - most_common > k:
                counts[s[start]] -= 1
                start += 1
                most_common = counts.most_common(1)[0][1]
                
            #Check if this window is the new longest
            res = max(res, end - start + 1)
                
        return res
        