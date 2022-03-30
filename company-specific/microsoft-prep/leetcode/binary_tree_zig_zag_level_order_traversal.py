from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # left -> right, remove from front of queue, add children to end left tjhen right
        
        # right -> left, remove from back of queue, add children to front of queue, right then left
        if not root: return []
        queue = deque()
        queue.append(root)
        res = []
        direction = 1
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                if direction == 1:
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                else:
                    node = queue.pop()
                    level.append(node.val)
                    if node.right: queue.appendleft(node.right)
                    if node.left: queue.appendleft(node.left)
            res.append(level)
            direction *= -1
        return res
                        
                
            
        