# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        s = ListNode(0)
        s.next = head
        pre = s
        cur = s.next
        while cur:
            if cur.next and cur.next.val == cur.val:
                temp = cur.val
                while cur and temp == cur.val:
                    cur = cur.next
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        pre.next = cur
        return s.next
