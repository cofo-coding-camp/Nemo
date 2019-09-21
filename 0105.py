# Definition for a binary tree node.# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left, right):
            nonlocal pre_idx
            if left == right:
                return None
            
            val = preorder[pre_idx]
            root = TreeNode(val)
            i = inorder.index(val)
            pre_idx += 1

            root.left = helper(left, i)
            root.right = helper(i + 1, right)
            return root
        
        pre_idx = 0
        return helper(0, len(inorder))
