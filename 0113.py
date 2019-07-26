# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        def helper(root, target, cache):
            if not root:
                return
            if not root.left and not root.right and root.val == target:
                cache += [root.val]
                res.append(cache)
                return
            helper(root.left, target - root.val, cache += [root.val])
            helper(root.right, target - root.val, cache += [root.val])
        res = []
        helper(root, sum, [])
        return res