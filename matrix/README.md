

## Matrix

- [X] [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
- [X] [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [X] [Rotate Image](https://leetcode.com/problems/rotate-image/)
- [X] [Word Search](https://leetcode.com/problems/word-search/)

---

### Set Matrix Zeroes ###
The solution for this problem was similar to O(1) space "Game of Life". In order to clear rows without overwriting original zeroes we can mark them with a different data type, or if the input is bounded we can use a negative integer. In order to avoid repeating operations where we clear rows and columns, I used a set to keep track of which rows and columns we have already cleared.

After each row and column is marked I just do the O(m * n) matrix traversal to see all grids that have been marked to zero. This is a costly operation but the asymptotic time complexity is still O(m*n) with O(1) space which is optimal for most matrix problems.
```python
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        cleared_rows = set()
        cleared_cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in cleared_rows:
                        cleared_rows.add(i)
                        for k in range(n):
                            if matrix[i][k] != 0: matrix[i][k] = 'CLEAR'
                    if j not in cleared_cols:
                        cleared_cols.add(j)
                        for k in range(m):
                            if matrix[k][j] != 0: matrix[k][j] = 'CLEAR'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'CLEAR':
                    matrix[i][j] = 0
```
---

### Spiral Matrix ###
The solution for this approach is pretty straight forward. We'll keep track of a top, bottom, left, and right value for rows and columns that we need to iterate over in a while loop. The issue here is handling edge cases at the end. We need to recognize that at the end of the spiral traversal there will a either a whole row (1 X m) or whole column (n X 1) that has not been traversed. We can handle both of these cases with a final for loop as shown below
```python
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        
        while left < right and top < bottom:
            for col in range(left, right):
                res.append(matrix[top][col])
            for row in range(top, bottom):
                res.append(matrix[row][right])
            for col in range(right, left, -1):
                res.append(matrix[bottom][col])
            for row in range(bottom, top, -1):
                res.append(matrix[row][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        # Handle edge cases where there is a remaining
        # row or column in the spiral matrix
        for row in range(top, bottom+1):
            for col in range(left, right+1):
                res.append(matrix[row][col])
        
        return res
```

### Rotate Image ###
The solution is to think about this rotation as swapping four values at a time. First we start in the outer square of the matrix and move inwards using the same iterative approach. The first rotation will always be rotation the four corners clockwise. We have to store a few of these in temp variables as we rotate them accordingly. We'll perform 1 less than than current out squares length rotations. After all values have been rotated in the outer square me increment left and right to move inwards and perform the same rotations

```python
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            t, b = l, r
            for i in range(r-l):    
                # Top row to right column
                top_right = matrix[t+i][r]
                matrix[t+i][r] = matrix[t][l+i]
        
                # Right column to bottom row
                bottom_right = matrix[b][r-i]
                matrix[b][r-i] = top_right
               
                # Bottom row to left column
                bottom_left = matrix[b-i][l]
                matrix[b-i][l] = bottom_right
             
                # Left column to top row
                matrix[t][l+i] = bottom_left
            l += 1
            r -= 1
```

### Word Search ###
Here is my iterative dfs solution. Use this example as a reference for how to handle dfs backtracking for iterative solutions.
Notice how I'm traversing the matrix to find all starting points and creating a new stack at each start point.
After each node has been marked as visited we also add a 'clone' of this node to the stack but marked as a backtracking node. This way when we pop it off the stack again on the backtracking portion we can remove it from the set of visited nodes so that it can be used again in the future.

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        neighbors = [(0,-1),(0,1),(-1,0),(1,0)]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    stack = []
                    stack.append((i,j,0,False))
                    visited = set()
                
                    while len(stack):
                        row, col, index, backtrack = stack.pop()
                        if backtrack: # skip this node if it is marked as backtracking node
                            visited.remove((row, col))
                            continue
                        if index == len(word) - 1: #at this point we have found our word
                            return True

                        # Mark as visited and add backtracking node
                        visited.add((row, col))
                        stack.append((row, col, index, True))
                    
                        for neighbor in neighbors:
                            dx, dy = neighbor
                            x, y = row + dx, col + dy
                            if (x,y) in visited: # Don't check neighbors if this node has been seen
                                continue
                            if x >= 0 and x < m and y >= 0 and y < n and board[x][y] == word[index+1]:
                                stack.append((x,y,index+1,False))
                                    
        return False     
```