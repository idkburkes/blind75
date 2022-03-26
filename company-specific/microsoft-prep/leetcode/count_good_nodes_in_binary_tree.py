# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution
def goodNodes(self, root: TreeNode) -> int:
    return self.countGoodNodes(root, root.val)

def countGoodNodes(self, root: TreeNode, maxnum: int) -> int:
    if root is None: return 0    
    goodNodesLeft = self.countGoodNodes(root.left, max(root.val, maxnum))
    goodNodesRight = self.countGoodNodes(root.right, max(root.val, maxnum))
    childGoodNodes = goodNodesLeft + goodNodesRight
    return childGoodNodes + 1 if root.val >= maxnum else childGoodNodes

# Iterative solution
def goodNodes(self, root: TreeNode) -> int:
    stack = [(root, float("-inf"))]
    res = 0
    while stack:
        node, max_so_far = stack.pop()
        if node.val >= max_so_far:
            res += 1
        if node.left:
            stack.append((node.left, max(max_so_far, node.val)))
        if node.right:
            stack.append((node.right, max(max_so_far, node.val)))
    return res