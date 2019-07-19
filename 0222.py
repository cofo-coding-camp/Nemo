class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1 - Recursive


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def foo(root):
            if not root:
                return 0
            left = foo(root.left)
            right = foo(root.right)
            return left + right + 1
        return foo(root)

# Solution 2 - Iterative


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        cache = [root]
        count = 0
        if not root:
            return 0
        while cache:
            node = cache.pop(0)
            count += 1
            if node.left:
                cache.append(node.left)
            if node.right:
                cache.append(node.right)
        return count


# Solution 3 - binary Search
class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        height = 0
        head = root
        while head:
            height += 1
            head = head.left

        low = 1 << (height - 1)
        high = (1 << height) - 1

        while low < high:
            m = mid = (low + high + 1) // 2
            path = []
            while m != 1:
                path.append(m)
                m = m // 2
            cur = 1
            head = root
            while head and path:
                if cur * 2 == path[-1]:
                    head = head.left
                else:
                    head = head.right
                cur = path.pop()
            
            if head:
                low = mid
            else:
                high = mid - 1
        return low

