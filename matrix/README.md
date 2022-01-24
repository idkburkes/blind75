

## Matrix

- [X] [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
- [X] [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [ ] [Rotate Image](https://leetcode.com/problems/rotate-image/)
- [ ] [Word Search](https://leetcode.com/problems/word-search/)

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