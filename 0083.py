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
        h = s
        cur = head
        store = set()
        while cur:
            if cur.val not in store:
                h.next = ListNode(cur.val)
                h = h.next
                store.add(cur.val)
            cur = cur.next
        
        return s.next