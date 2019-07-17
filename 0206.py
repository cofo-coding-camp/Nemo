# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

<<<<<<< HEAD
# Solution - 1 Iteration
=======
# Solution - 1 Iterative
>>>>>>> 673f03c64a73be07006e94c7fd6627e5a17ced07


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
<<<<<<< HEAD
        if not head or head.next:
=======
        if not head or not head.next:
>>>>>>> 673f03c64a73be07006e94c7fd6627e5a17ced07
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
<<<<<<< HEAD
        return res
=======
        return res
>>>>>>> 673f03c64a73be07006e94c7fd6627e5a17ced07
