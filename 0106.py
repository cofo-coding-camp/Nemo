# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left, right):
            nonlocal post_idx
            if left == right:
                return None
            
            val = postorder[post_idx]
            root = TreeNode(val)
            i = inorder.index(val)
            post_idx -= 1

            root.right = helper(i + 1, right)
            root.left = helper(left, i)
            return root
            
        post_idx = len(postorder) - 1
        return helper(0, len(inorder))