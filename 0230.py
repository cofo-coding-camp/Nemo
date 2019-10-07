# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = None
        def helper(root):
            nonlocal res, k
            if root.left:
                helper(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return res
            if root.right:
                helper(root.right)
        
        helper(root)
        return res