# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.nxet
            fast = fast.next.next
            if slow == fast:
                return True
        return False
