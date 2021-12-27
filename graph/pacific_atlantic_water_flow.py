#  I really struggled on this one. Need to practice graph problems more.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights[0]) #rows
        m = len(heights) #cols
        pacificVisited = [[False for col in range(n)] for row in range(m)]
        atlanticVisited = [[False for col in range(n)] for row in range(m)]

        # prepopulate both graphs
        atlanticQ, pacificQ = [], []
        for i in range(m):
            pacificVisited[i][0] = True
            atlanticVisited[i][n-1] = True
            pacificQ.append((i,0))
            atlanticQ.append((i,n-1))
        for i in range(n):
            pacificVisited[0][i] = True
            atlanticVisited[m-1][i] = True
            pacificQ.append((0,i))
            atlanticQ.append((m-1,i))
        self.bfs(heights, pacificQ, pacificVisited, m, n)
        self.bfs(heights, atlanticQ, atlanticVisited, m, n)    
        res = []
        for i in range(m):
            for j in range(n):
                if pacificVisited[i][j] == True and atlanticVisited[i][j] == True:
                    res.append([i,j])
        return res

    def bfs(self, heights, queue, visited, m, n):
        while queue:
            i,j = queue.pop(0)
            if i > 0 and heights[i-1][j] >= heights[i][j] and visited[i-1][j] == False: #up
                queue.append((i-1, j))
            if i < m-1 and heights[i+1][j] >= heights[i][j] and visited[i+1][j] == False: #down
                queue.append((i+1, j))
            if j > 0 and heights[i][j-1] >= heights[i][j] and visited[i][j-1] == False: #left
                queue.append((i,j-1))
            if j < n-1 and heights[i][j+1] >= heights[i][j] and visited[i][j+1] == False: #right
                queue.append((i,j+1))
            visited[i][j] = True
            
