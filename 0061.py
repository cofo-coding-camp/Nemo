# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1

        tail.next = head
        cur = head
        for _ in range(l - k % l - 1):
            cur = cur.next

        head = cur.next
        cur.next = None

        return head