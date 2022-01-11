# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [[root.val]]
        res, queue = [], []
        queue.append(root)
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node.val)
            res.append(level)
        return res
