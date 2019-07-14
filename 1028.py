# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def foo(s, depth):
            d = 0

            while self.idx < len(s) and s[self.idx] == '-':
                self.idx += 1
                d += 1
            
            if d != depth:
                self.idx -= d
                return None
            
            val = 0
            while self.idx < len(s) and s[self.idx].isdigit():
                val = val * 10 + int(s[self.idx])
                self.idx += 1

            root = TreeNode(val)
            root.left = foo(s, depth + 1)
            root.right = foo(s, depth + 1)
            return root
        
        self.idx = 0
        return foo(S, 0)