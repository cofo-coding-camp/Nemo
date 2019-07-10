# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def foo(root, s):
            if not root:
                s += 'None,'
            else:
                s += str(root.val) + ','
                s = foo(root.left, s)
                s = foo(root.right, s)
            return s
        return foo(root, '')
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def bar(l):
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = bar(l)
            root.right = bar(l)
            return root

        data_list = data.split(',')
        root = bar(data_list)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))