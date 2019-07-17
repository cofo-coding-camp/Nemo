# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(0)
        large = ListNode(0)
        p_large = large
        p_small = small
        cur = head
        while cur:
            if cur.val < x:
                p_small.next = ListNode(cur.val)
                p_small = p_small.next
            else:
                p_large.next = ListNode(cur.val)
                p_large = p_large.next
            cur = cur.next
        p_small.next = large.next
        return small.next