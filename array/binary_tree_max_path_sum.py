# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if root is None: return 0
        if not root.left and not root.right: return root.val

        # Set global max to negative infinity instead of 0 so we can handle negative numbers as the max properly
        self.globalmax = float('-inf')
        
        def get_path(node):
            if not node: return 0 # base case for end of paths
             
            # Ignore sub tree paths that have a negative sum
            left = max(get_path(node.left), 0)
            right = max(get_path(node.right), 0)

            # New global max when the current node + left and right subtree path sums are higher   
            self.globalmax = max(self.globalmax, left + right + node.val)
            
            # Since we can only take a single path we'll return the max between left or right plus the current node
            return max(left + node.val, right + node.val)
        
        get_path(root)
        return self.globalmax
            
        
        
        