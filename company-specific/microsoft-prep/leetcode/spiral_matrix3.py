class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i, j = rStart, cStart
        res = [[i, j]]
        
        if rows * cols == 1:
            return res
        # right, down, left, up 
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0                   
        
        while len(res) < rows * cols:
                # perform steps 1,1,2,2,3,3,4,4...
                for k in range(1,2*max(rows,cols)):
                    for _ in range(2): # go in next 2 directions
                        for _ in range(k): # traverse in this directions k times
                            direction = directions[d]
                            i += direction[0]
                            j += direction[1]
                            if 0 <= i < rows and 0 <= j < cols:
                                res.append([i,j])
                                if len(res) == rows * cols:
                                    return res
                        d = (d + 1) % 4
                    
                # step in direction k times, then step in next direction k times
                
                
                
                
        
        
        