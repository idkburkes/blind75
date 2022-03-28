def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    res = []
    
    while left < right and top < bottom:
        # top row
        for col in range(left, right):
            res.append(matrix[top][col])
        
        # right column (downwards)
        for row in range(top, bottom):
            res.append(matrix[row][right])
        
        # bottom row
        for col in range(right, left, -1):
            res.append(matrix[bottom][col])
        
        # left column (upwards)
        for row in range(bottom, top, -1):
            res.append(matrix[row][left])
            
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    
    for col in range(left, right + 1):
        for row in range(top, bottom + 1):
            res.append(matrix[row][col])
            
    return res