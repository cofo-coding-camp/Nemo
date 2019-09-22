# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root, s):
            nonlocal res
            if not root:
                return
            if not root.left and not root.right:
                res += int(s + str(root.val))
                return
            dfs(root.left, s + str(root.val))
            dfs(root.right, s + str(root.val))
        res = 0
        dfs(root, '')

        return res