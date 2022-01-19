# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution is to perform an inorder traversal then return the Kth number evaluated
# recursive solution is trivial, so I'll try the iterative solution afterwards
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inOrder(root, res)
        return res[k-1]
        
    
    def inOrder(self, root, res):
        if root is None: return
        
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)


# Here is the iterative solution

class SolutionIterative:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = 0
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k: return node.val
            cur = cur.right
            

            

            
        
        
        
        
    
        

        
        
            
            
            
        
        
