class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''
        stack = []
        
        
        for i in range(len(s)):
            char = s[i]
            if char != ']':
                stack.append(char)
            else:
                group = ''
                while stack and stack[-1] != '[':
                    group = stack.pop() + group

                stack.pop() # remove open bracket
                
                n = times = 0
                while stack and stack[-1].isdigit(): # get number before open bracket
                    times +=  (10**n) * int(stack.pop())
                    n += 1
                    
                for _ in range(times):
                    stack.append(group)
    
        res = ''
        while stack:
            res = stack.pop() + res
    
        return res
    
    
            
                
                
        
         
        
        
        
        