"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        queue = [node]
        nodemap = {node: Node(node.val)}
        while queue:
            n = queue.pop(0)
            for neighbor in n.neighbors:
                if neighbor not in nodemap:
                    queue.append(neighbor)
                    nodemap[neighbor] = Node(neighbor.val)
                nodemap[n].neighbors.append(nodemap[neighbor]) 
        return nodemap[node]
            
            
                
        
        
        
        
        