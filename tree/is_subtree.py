# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot): return True
        elif not root: return False
        return self.isMatch(root.left, subRoot) or self.isMatch(root.right, subRoot)

    def isMatch(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q
        return p.val == q.val and self.isMatch(p.left, q.left) and self.isMatch(p.right, q.right)

        

        

            

                

        
