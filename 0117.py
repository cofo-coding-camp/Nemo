"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        head = None
        tail = None
        while cur:
            while cur:
                if cur.left:
                    if not head:
                        head = cur.left
                        tail = cur.left
                    else:
                        tail.next = cur.left
                        tail = tail.next
                if cur.right:
                    if not head:
                        head = cur.right
                        tail = cur.right
                    else:
                        tail.next = cur.right
                        tail = tail.next
                cur = cur.next
            cur = head
            head = None
            head = None
        
        return root