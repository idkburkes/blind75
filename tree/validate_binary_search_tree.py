# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], lessThan = float('inf'), greaterThan = -float('inf')) -> bool:
        if not root:
            return True
        elif root.val >= lessThan or root.val <= greaterThan:
            return False
        else:
            return self.isValidBST(root.left, min(root.val, lessThan), greaterThan) and self.isValidBST(root.right, lessThan, max(root.val, greaterThan))
        
        
                
 