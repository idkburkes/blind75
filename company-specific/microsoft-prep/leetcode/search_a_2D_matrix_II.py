class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(min(m,n)):
            in_row = self.binarySearch(matrix, target, i, False)
            in_col = self.binarySearch(matrix, target, i, True)
            if in_row or in_col:
                return True
        return False
            
             
    def binarySearch(self, matrix, target, i, vertical):
        
        left = i
        right = len(matrix) - 1 if vertical else len(matrix[0]) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if vertical:
                if matrix[mid][i] == target:
                    return True
                elif matrix[mid][i] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left= mid + 1
        return False