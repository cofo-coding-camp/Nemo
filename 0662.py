# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = [[0, root]]
        res = 1

        while q:
            res = max(res, q[-1][0] - q[0][0] + 1)
            temp = []

            for i, r in q:
                if r.left:
                    temp += [[i * 2, r.left]]
                if r.right:
                    temp += [[i * 2 + 1, r.right]]
            q = temp
        
        return res