class Solution:
    def minOperations(self, s: str) -> int:
        
        count1 = count2 = 0
        # alternating string either starts with 0 or 1
        # ex) 0101, 1010
        # count how many differences the string has between both of these
        # whichever is smaller will be the min changes
        
        for i in range(len(s)):
            z = str(i%2)
            if z == str(s[i]):
                count1 += 1
            else:
                count2 += 1
                
        return min(count1, count2)
            
        
        