# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hashmap = dict()
        self.max_h = float('-inf')
        self.min_h = float('inf')
        def dfs(root, level_h, level_v):
            self.max_h = max(level_h, self.max_h)
            self.min_h = min(level_h, self.min_h)
            hashmap[level_h] = hashmap.get(level_h, list())
            hashmap[level_h].append((level_v, root.val))
            if root.left:
                dfs(root.left, level_h - 1, level_v + 1)
            if root.right:
                dfs(root.right, level_h + 1, level_v + 1)
        
        dfs(root, 0, 0)
        res = []
        for i in range(self.min_h, self.max_h + 1):
            res.append( [j for i,j in sorted(hashmap[i])])
        
        return res
            
            
            
            
        
        