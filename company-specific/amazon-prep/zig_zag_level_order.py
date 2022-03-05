from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dq = deque()
        res = []
        dq.append(root)
        direction = 1
        while len(dq):
            level = []
            for _ in range(len(dq)):
                if direction == 1:
                    node = dq.popleft()
                    level.append(node.val)
                    if node.left: dq.append(node.left)
                    if node.right: dq.append(node.right)
                else:
                    node = dq.pop()
                    level.append(node.val)
                    if node.right: dq.appendleft(node.right)
                    if node.left: dq.appendleft(node.left)
            direction *= -1
            res.append(level)
        return res
                    
            
        
        
        
        