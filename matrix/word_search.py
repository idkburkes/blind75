class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        neighbors = [(0,-1),(0,1),(-1,0),(1,0)]
        startpoints = []
        
        # Find all starting points
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    startpoints.append((i, j, 0, False))
                
        for startpoint in startpoints:
                stack, visited = [], set()
                stack.append(startpoint)
                
                while len(stack):
                    row, col, index, backtrack = stack.pop()
                    if backtrack:
                        visited.remove((row, col))
                        continue
                    if index == len(word) - 1:
                        return True
                    
                    # Mark as visited and add backtracking node 
                    visited.add((row, col))
                    stack.append((row, col, index, True))
                    
                    for neighbor in neighbors:
                        dx, dy = neighbor
                        x, y = row + dx, col + dy
                        if (x,y) in visited: # don't check neighbors if this node has been seen
                            continue
                        if x >= 0 and x < m and y >= 0 and y < n and board[x][y] == word[index+1]:
                            stack.append((x,y,index+1,False)) # Add regular forward moving node            
        return False
                        
                        
                    
                    
                
               
                
                
                
                
        