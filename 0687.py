# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        
        def foo(root):
            if not root:
                return 0
            left = foo(root.left)
            right = foo(root.right)
            left_len = right_len = 0
            if root.left and root.left.val == root.val:
                left_len = left + 1
            if root.right and root.right.val == root.val:
                right_len = right + 1
            self.res = max(self.res, left_len + right_len)
            return max(left_len, right_len)
        
        foo(root)
        return self.res