

class Solution:
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