class Solution:
    def maxValue(self, n: str, x: int) -> str:
        res = ''
        inserted = False
        positive = True if int(n) > 0 else False
        
        if positive:
            for i in range(len(n)):
                if not inserted and int(n[i]) < x:
                    res += str(x)
                    inserted = True
                res += n[i]
        else:
            res += '-'
            for i in range(1,len(n)):
                if not inserted and int(n[i]) > x:
                    res += str(x)
                    inserted = True
                res += n[i]
        
        if not inserted: res += str(x)
        return res
            
            
            
            
        