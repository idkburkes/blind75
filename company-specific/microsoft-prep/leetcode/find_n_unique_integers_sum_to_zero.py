class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        even = n % 2 == 0     
        sign = 1
        limit = n + 2 if even else n + 1
        res = []

        if n % 2 != 0:
            res.append(0)
    
        for i in range(2, limit):
            num = (i // 2) * sign
            res.append(num)
            sign *= -1
        
        return res
        
                
                
        