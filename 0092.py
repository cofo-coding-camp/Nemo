# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 1
        cur = head
        if m == n:
            return head
        while count < m:
            first = cur
            cur = cur.next
            count += 1
        pre = None
        last = cur
        while count <= n:
            cur.next, pre, cur = pre, cur, cur.next
            count += 1
        last.next = cur
        if m != 1:
            first.next = pre
            return head
        else:
            return pre
