# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def foo(cur):
            if not cur:
                return 0
            left = foo(cur.left)
            right = foo(cur.right)
            found = cur == p or cur == q
            if left + right + found == 2:
                self.res = cur
            return found or left or right
        foo(root)
        return self.res