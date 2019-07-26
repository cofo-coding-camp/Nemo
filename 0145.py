# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1 - Iterative


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cache = [root]
        res = []
        while cache:
            root = cache.pop()
            res.append(root.val)
            if root.left:
                cache.append(root.left)
            if root.right:
                cache.append(root.right)
        
        return res[::-1]

# Solution 2 - Recursive


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def DFS(root):    
            if not root:
                return
            DFS(root.left)
            DFS(root.right)
            res.append(root.val)
        DFS(root)
        return res

# Solution 3 - Iterative 2


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        cache = [root]

        while cache:
            if not cache[-1].left and not cache[-1].right:
                cur = cache.pop()
                res.append(cur.val)
                if not cache:
                    break
            last = cache[-1]
            if last.right:
                cache.append(last.right)
                last.right = None
            if last.left:
                cache.append(last.left)
                last.left = None
        
        return res