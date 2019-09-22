# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            nonlocal max_sum
            if not root:
                return 0

            left = max(helper(root.left), 0)
            right = max(helper(root.right), 0)

            price = root.val + left + right

            max_sum = max(max_sum, price)
            return root.val + max(left, right)
        
        max_sum = float('-inf')
        helper(root)
        return max_sum