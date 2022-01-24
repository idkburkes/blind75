class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        
        while top < bottom and left < right:
            # append top row
            for col in range(left, right):
                res.append(matrix[top][col])
            
            # append right column
            for row in range(top, bottom):
                res.append(matrix[row][right])
            
            # append bottom row
            for col in range(right, left, -1):
                res.append(matrix[bottom][col])
            
            # append left column
            for row in range(bottom, top, -1):
                res.append(matrix[row][left])
            
            # move inward
            left, right, bottom, top = left + 1, right - 1, bottom - 1, top + 1
         
        for row in range(top, bottom+1):
            for col in range(left, right+1):
                res.append(matrix[row][col])
        return res
        