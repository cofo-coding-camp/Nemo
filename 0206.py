# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution - 1 Iteration


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

# Solution - 2 Recursive


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res