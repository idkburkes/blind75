class Solution:
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