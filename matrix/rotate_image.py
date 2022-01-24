class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
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
        