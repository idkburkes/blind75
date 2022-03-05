class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = []
        dirs = [(0,1), (-1,0), (0,-1), (1,0)]
        freshOranges = 0
        badOranges = 0
        
        # Counts fresh oranges and puts bad oranges in queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                    badOranges += 1
                    
        if freshOranges == 0:
            return 0
        elif badOranges == 0:
            return -1
        
        queue_size = len(queue)
        timestamp = -1
        
        while len(queue):
            for _ in range(queue_size):
                row, col = queue.pop(0)
                for d in dirs:
                    neirow = row + d[0]
                    neicol = col + d[1]
                    if m > neirow >= 0 and n > neicol >= 0:
                        if grid[neirow][neicol] == 1:
                            grid[neirow][neicol] = 2
                            freshOranges -= 1
                            queue.append((neirow, neicol))
            timestamp += 1
            queue_size = len(queue)
            
        return timestamp if freshOranges == 0 else -1
                
                    
                
        