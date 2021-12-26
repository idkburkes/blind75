class Solution:
    # Iterative DFS
    # Time - O(mXn)
    # Space - O(mXn)
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numIslands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    stack = [(row,col)]
                    while len(stack):
                        curRow, curCol = stack.pop()
                        if curRow > 0 and grid[curRow - 1][curCol] == '1': #add neighbor up
                            stack.append((curRow-1, curCol))
                        if curRow < rows - 1 and grid[curRow + 1][curCol] == '1': #add neighbor down
                            stack.append((curRow+1, curCol))
                        if curCol > 0 and grid[curRow][curCol - 1] == '1':  #add neighbor left
                            stack.append((curRow, curCol-1))
                        if curCol < cols - 1 and grid[curRow][curCol + 1] == '1':#add neighbor right
                            stack.append((curRow, curCol+1))
                        grid[curRow][curCol] = '0'
                    numIslands += 1
        return numIslands