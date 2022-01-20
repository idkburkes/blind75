

## Matrix

- [X] [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
- [ ] [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [ ] [Rotate Image](https://leetcode.com/problems/rotate-image/)
- [ ] [Word Search](https://leetcode.com/problems/word-search/)


### Set Matrix Zeroes ###
The solution for this problem was similar to O(1) space "Game of Life". In order to clear rows without overwriting original zeroes we can mark them with a different data type, or if the input is bounded we can use a negative integer. In order to avoid repeating operations where we clear rows and columns, I used a set to keep track of which rows and columns we have already cleared.

After each row and column is marked I just do the O(m * n) matrix traversal to see all grids that have been marked to zero. This is a costly operation but the asymptotic time complexity is still O(m*n) with O(1) space which is optimal for most matrix problems.

---