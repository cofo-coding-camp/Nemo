class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.e1 = None
        self.e2 = None
        self.pre = TreeNode(-float('inf'))

        def DFS(root):
            if not root:
                return
            DFS(root.left)
            if not self.e1 and self.pre.val > root.val:
                self.e1 = self.pre
            if self.e1 and self.pre.val > root.val:
                self.e2 = root
            self.pre = root
            DFS(root.right)

        DFS(root)
        self.e1.val, self.e2.val = self.e2.val, self.e1.val