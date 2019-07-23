# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        depth = float('inf')
        if root.left:
            depth = min(self.minDepth(root.left), depth)
        if root.right:
            depth = min(self.minDepth(root.right), depth)
        return depth + 1