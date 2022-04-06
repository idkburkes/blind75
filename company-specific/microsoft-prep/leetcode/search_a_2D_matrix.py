class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            i, j = self.convertToGrid(mid, n)
        
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
                 
    def convertToGrid(self, num, rowLen):
        row = num // rowLen
        col = num % rowLen
        return row, col
        
        