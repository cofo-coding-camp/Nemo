# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


# Solution - 1 Hash Map O(n)


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        hash_map = {}
        new_head = Node(0, None, None)
        new_cur = new_head
        cur = head
        while cur:
            new_cur.next = Node(cur.val, None, None)
            new_cur = new_cur.next
            hash_map[cur] = new_cur
            cur = cur.next

        cur = head
        new_cur = new_head.next
        while cur:
            if cur.random:
                new_cur.random = hash_map[cur.random]
            cur = cur.next
            new_cur = new_cur.next
        return new_head.next


# Solutoion - 2 O(1)
# TODO:debug
'''
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        new_head = Node(0, None, None)
        new_cur = new_head
        cur = head
        while cur:
            new_cur.next = Node(cur.val, None, None)
            new_cur = new_cur.next
            new_cur.random = cur
            temp = cur.next
            cur.next = new_cur
            cur = temp

        cur = head
        new_cur = new_head.next
        while new_cur:
            if new_cur.random.random:
                new_cur.random = new_cur.random.random.next
            else:
                new_cur.random = None
            new_cur = new_cur.next

        return new_head.next
'''