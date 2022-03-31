"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root: return
        queue = [root]
        node = None
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                if node is None:
                    node = queue.pop(0)                
                next = None
                if queue and i < level_size - 1:
                    next = queue.pop(0)
                    
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                node.next = next
                node = next
        return root
                
                
            
        