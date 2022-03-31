# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        res = ''
        queue = [root]
        idx = 0
        
        while queue:
            node = queue.pop(0)
            
            if not node:
                res += 'null,'
                continue
                
            res += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
                
        return res
            
            
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split(',')
        n = len(data)
        i = level_size = 1
        root = TreeNode(data[0])
        queue = [root]

        while i < n:
            for _ in range(level_size):
                node = queue.pop(0)
                
                if i < n and data[i]:
                    left_node = TreeNode(data[i])
                    node.left = left_node
                    queue.append(left_node)
                i += 1
                
                if  i < n and data[i]:
                    right_node = TreeNode(data[i])
                    node.right = right_node
                    queue.append(right_node)
                i += 1
                
            # go to next level
            level_size *= 2
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))